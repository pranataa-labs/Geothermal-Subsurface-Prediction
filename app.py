from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Direktori basis tempat app.py dan model berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Model Hybrid dan Scaler terbaru yang ada di folder artikel/model
MODEL_PATH = os.path.join(BASE_DIR, 'model_geotermal_hybrid.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'scaler_geotermal.pkl')

print("Memuat scaler...")
scaler = joblib.load(SCALER_PATH)
print("Memuat model hybrid...")
model = joblib.load(MODEL_PATH)
print("Model dan Scaler berhasil dimuat!")

@app.route('/', methods=['GET', 'POST'])
def index():
    # 1. Tampilan Awal (GET)
    if request.method == 'GET':
        return render_template('index.html')
        
    # 2. Eksekusi Prediksi (POST)
    if request.method == 'POST':
        try:
            # Mengambil 10 fitur input
            vp_7000m = float(request.form['vp_7000'])
            crustal_thickness = float(request.form['crustal_thickness'])
            dvs_20km = float(request.form['dvs_20km'])
            vp_6000m = float(request.form['vp_6000m'])
            vpvs_60km = float(request.form['vpvs_60km'])
            dvs_60km = float(request.form['dvs_60km'])
            gg_mantle_60km = float(request.form['gg_mantle_60km'])
            dvpvs_60km = float(request.form['dvpvs_60km'])
            dvs_40km = float(request.form['dvs_40km'])
            elevation_detrend = float(request.form['elevation_detrend'])

            input_data = [[
                vp_7000m, crustal_thickness, dvs_20km, vp_6000m, vpvs_60km, 
                dvs_60km, gg_mantle_60km, dvpvs_60km, dvs_40km, elevation_detrend
            ]]

            # Normalisasi
            input_scaled = scaler.transform(input_data)

            # Eksekusi Inferensi Model
            prediksi = model.predict(input_scaled)
            
            # Format list suhu kedalaman (1000m - 5000m)
            prediksi_suhu = np.round(prediksi[0], 2).tolist()

            suhu_5000m = prediksi_suhu[4]
            if suhu_5000m >= 220:
                rekomendasi = {'status': 'Highly Prospective', 'desc': 'Ideal temperature for Flash Steam power plants.', 'color': 'success'}
            elif suhu_5000m >= 150:
                rekomendasi = {'status': 'Moderately Prospective', 'desc': 'Sufficient temperature for Binary Cycle power plants.', 'color': 'warning'}
            else:
                rekomendasi = {'status': 'High Risk', 'desc': 'Reservoir temperature below threshold (Dry Hole).', 'color': 'danger'}
                
            return render_template('index.html', prediksi_suhu=prediksi_suhu, rekomendasi=rekomendasi)
        except Exception as e:
            return f"Internal Error: {e}. Make sure all parameters are filled with numbers.", 400

if __name__ == '__main__':
    # use_reloader=False agar model 2GB tidak dimuat 2x di memori
    app.run(debug=True, use_reloader=False, port=5000)
