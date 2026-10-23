# 🌋 Geothermal Subsurface Temperature Profile Prediction

Web application for predicting multi-depth subsurface geothermal temperature profiles (1,000m to 5,000m) based on earth science features using a Multi-Output Hybrid Stacking Ensemble (Random Forest + XGBoost).

---

## ⚡ Key Predictive Features

- **Multi-Depth Prediction:** Predicts reservoir temperatures at depths of 1,000m, 2,000m, 3,000m, 4,000m, and 5,000m simultaneously.
- **Hybrid Ensemble Machine Learning:** Combines Random Forest and XGBoost base estimators through Stacking Regression.
- **Geothermal Gradient Visualization:** Interactive temperature gradient depth curve using Plotly with dynamic heatmap color-coding.
- **Prospectivity Assessment:** Automatically classifies geothermal commercial potential (*Highly Prospective, Moderately Prospective, or High Risk*).

---

## 🔬 Input Geophysical Feature Parameters (10 Dimensions)

1. `Vp_7000m`: P-wave velocity at 7,000m depth (km/s)
2. `crustal_thickness`: Crustal thickness (km)
3. `dVs_20km`: S-wave velocity anomaly at 20km depth (%)
4. `Vp_6000m`: P-wave velocity at 6,000m depth (km/s)
5. `VpVs_60km`: Vp/Vs ratio at 60km depth
6. `dVs_60km`: S-wave velocity anomaly at 60km depth (%)
7. `gg_mantle_60km`: Geothermal gradient mantle proxy at 60km depth
8. `dVpVs_60km`: Vp/Vs velocity anomaly at 60km depth (%)
9. `dVs_40km`: S-wave velocity anomaly at 40km depth (%)
10. `elevation_detrend`: Topographic elevation detrended (m)

---

## 📦 Serialized Machine Learning Artifacts

> **Note:** The serialized model file `model_geotermal_hybrid.pkl` (~2.05 GB) exceeds GitHub's 100 MB upload limit and is excluded from git tracking via `.gitignore`.
> Place `model_geotermal_hybrid.pkl` and `scaler_geotermal.pkl` in the root directory before running the application.

---

## 🚀 Local Installation & Setup Guide

### 1. Repository Cloning
```bash
git clone https://github.com/pranataa-labs/Geothermal-Subsurface-Prediction.git
cd Geothermal-Subsurface-Prediction
```

### 2. Virtual Environment Configuration
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Dependency Installation
```bash
pip install -r requirements.txt
```

### 4. Launch Web Application
```bash
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
