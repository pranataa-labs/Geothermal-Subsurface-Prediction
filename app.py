from flask import Flask, render_template, request
import joblib
import numpy as np
import os
import time

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model_geotermal_hybrid.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'scaler_geotermal.pkl')

print("Memuat scaler...")
scaler = joblib.load(SCALER_PATH)
print("Memuat model hybrid...")
model = joblib.load(MODEL_PATH)
print("Model dan Scaler berhasil dimuat!")

# Rentang fisik empiris berdasarkan dataset Conterminous US (N = 200,000)
FEATURE_SPECS = [
    ('vp_7000', 'Vp_7000m (km/s)', 3.49, 6.56),
    ('crustal_thickness', 'crustal_thickness (km)', 20.30, 54.75),
    ('dvs_20km', 'dVs_20km (%)', -1.67, 8.18),
    ('vp_6000m', 'Vp_6000m (km/s)', 3.49, 6.56),
    ('vpvs_60km', 'VpVs_60km (ratio)', 1.72, 1.81),
    ('dvs_60km', 'dVs_60km (%)', -4.57, 6.52),
    ('gg_mantle_60km', 'gg_mantle_60km (°C/km)', 4.51, 21.93),
    ('dvpvs_60km', 'dVpVs_60km (%)', -2.58, 1.45),
    ('dvs_40km', 'dVs_40km (%)', -3.17, 8.35),
    ('elevation_detrend', 'elevation_detrend (m)', -789.0, 984.0)
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', feature_specs=FEATURE_SPECS)

    if request.method == 'POST':
        input_values = []
        warnings_list = []

        for field_name, label, f_min, f_max in FEATURE_SPECS:
            raw_val = request.form.get(field_name, '').strip().replace(',', '.')
            if raw_val == '':
                return render_template(
                    'index.html',
                    error_msg=f"Missing input parameter: {label}. All 10 geophysical predictors are required.",
                    feature_specs=FEATURE_SPECS
                ), 400
            try:
                val = float(raw_val)
            except ValueError:
                return render_template(
                    'index.html',
                    error_msg=f"Invalid non-numeric input for {label}: '{raw_val}'.",
                    feature_specs=FEATURE_SPECS
                ), 400

            if not np.isfinite(val):
                return render_template(
                    'index.html',
                    error_msg=f"Non-finite value detected for {label}.",
                    feature_specs=FEATURE_SPECS
                ), 400

            # Hard physical bounds check
            if field_name in ('vp_7000', 'vp_6000m') and (val <= 0 or val > 12.0):
                return render_template(
                    'index.html',
                    error_msg=f"Physically implausible seismic P-wave velocity for {label}: {val} km/s (valid domain: {f_min} to {f_max} km/s).",
                    feature_specs=FEATURE_SPECS
                ), 400
            if field_name == 'crustal_thickness' and (val < 5.0 or val > 90.0):
                return render_template(
                    'index.html',
                    error_msg=f"Physically implausible crustal thickness: {val} km (valid domain: {f_min} to {f_max} km).",
                    feature_specs=FEATURE_SPECS
                ), 400

            # Empirical calibration domain warning (out-of-distribution check)
            if val < f_min or val > f_max:
                warnings_list.append(
                    f"{label} ({val}) is outside the empirical Conterminous US calibration range [{f_min}, {f_max}]. Extrapolation uncertainty may increase."
                )

            input_values.append(val)

        t_start = time.perf_counter()
        input_scaled = scaler.transform([input_values])
        prediksi = model.predict(input_scaled)
        latency_ms = round((time.perf_counter() - t_start) * 1000.0, 2)

        prediksi_suhu = np.round(prediksi[0], 2).tolist()
        gradients = [round(prediksi_suhu[i+1] - prediksi_suhu[i], 2) for i in range(4)]
        mean_gradient = round(float(np.mean(gradients)), 2)

        suhu_5000m = prediksi_suhu[4]
        if suhu_5000m >= 220:
            rekomendasi = {
                'status': 'High-Enthalpy Thermal Prospect (Preliminary Screening)',
                'desc': f'Estimated 5000m temperature ({suhu_5000m} °C) and mean vertical gradient ({mean_gradient} °C/km) indicate favorable thermal potential for flash/dry-steam resource evaluation, subject to local permeability and fluid verification.',
                'color': 'success'
            }
        elif suhu_5000m >= 150:
            rekomendasi = {
                'status': 'Medium-Enthalpy Thermal Prospect (Preliminary Screening)',
                'desc': f'Estimated 5000m temperature ({suhu_5000m} °C) and mean vertical gradient ({mean_gradient} °C/km) are suitable for binary-cycle (ORC) or EGS pre-feasibility screening.',
                'color': 'warning'
            }
        else:
            rekomendasi = {
                'status': 'Low-Enthalpy / Baseline Conductive Regime',
                'desc': f'Estimated 5000m temperature ({suhu_5000m} °C; mean gradient {mean_gradient} °C/km) is below commercial power-generation thresholds.',
                'color': 'secondary'
            }

        return render_template(
            'index.html',
            prediksi_suhu=prediksi_suhu,
            rekomendasi=rekomendasi,
            latency_ms=latency_ms,
            mean_gradient=mean_gradient,
            warnings_list=warnings_list,
            feature_specs=FEATURE_SPECS
        )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)
