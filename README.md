# 🌋 Multi-Output Hybrid Ensemble for Geothermal Subsurface Temperature Profiles

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Framework Flask](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Google Drive Artifacts](https://img.shields.io/badge/Google%20Drive-Artifacts%20%26%20Model-orange.svg)](https://drive.google.com/drive/folders/1eAcN74KvVi5Pjj2qIRBgYzUZwVC3m7qV?usp=sharing)

Official codebase and interactive web dashboard accompanying the research article:  
**"Multi-Output Hybrid Ensemble Application for Predicting Geothermal Subsurface Temperature Profiles"**  
*Authors: Muhammad Aria Sastra and Suyud Widiono*  
*Informatics Study Program, Faculty of Science and Technology, Universitas Teknologi Yogyakarta*

---

## 📥 Reviewer Resources & Large Artifacts Download

Due to GitHub's 100 MB individual file upload limit, the large serialized machine learning model (`model_geotermal_hybrid.pkl`, ~976 MB) and full benchmark dataset (`dataset_200k_with_coords.csv`, ~41 MB) are hosted on Google Drive:

👉 **[Download Reviewer Artifacts on Google Drive](https://drive.google.com/drive/folders/1eAcN74KvVi5Pjj2qIRBgYzUZwVC3m7qV?usp=sharing)**

### Contents of the Google Drive Folder:
1. `model_geotermal_hybrid.pkl` (976 MB): Serialized Multi-Output Hybrid Stacking Regressor (Random Forest + XGBoost with depth-specific OLS meta-learners, $N = 200,000$).
2. `scaler_geotermal.pkl` (855 B): Serialized `StandardScaler` fitted on the 10 geophysical input dimensions.
3. `dataset_200k_with_coords.csv` (41.1 MB): Extracted benchmark dataset from the Stanford Thermal Earth Model (STEM-US).
4. `output_revisi/`: Directory containing all high-resolution figures (`Figure_1_Revised_Architecture.png`, `Figure_5_Revised_Flask_Dashboard.png`, SHAP summary plots, Taylor diagram) and verification spreadsheets (Tables 1–7 in `.xlsx`).

---

## 🌟 Key Highlights & Architectural Features

- **Multi-Depth Simultaneous Inference**: Predicts continuous subsurface temperatures across five depth horizons ($1,000\text{ m}, 2,000\text{ m}, 3,000\text{ m}, 4,000\text{ m}, 5,000\text{ m}$) simultaneously.
- **Hybrid Stacking Meta-Learner**: Combines tree-based bagging (Random Forest) and gradient boosting (XGBoost) through depth-specific Multiple Linear Regression meta-learners optimized via Bayesian Tree-structured Parzen Estimator (TPE) in Optuna.
- **Physical Plausibility & Gradient Analysis**: Evaluates vertical temperature gradients ($\Delta T / \Delta z$) and enforces zero temperature inversions ($0.0000\%$ violation rate across 200,000 profiles).
- **Spatial Block Cross-Validation**: Validates spatial generalizability on geographically disjoint $K$-means regional clusters ($\text{RMSE} = 5.97 \pm 0.28\text{ }^\circ\text{C}$, $R^2 = 84.41\%$).
- **Interactive Decision-Support Dashboard**: Web interface with real-time inference latency (~1–3 ms), dynamic empirical out-of-distribution warnings, vertical thermal gradient curves, and commercial enthalpy prospectivity classification.

---

## 🔬 10 Input Geophysical Predictor Dimensions

| Feature Symbol | Description | Valid Physical Domain |
| :--- | :--- | :---: |
| `Vp_7000m` | P-wave seismic velocity at 7,000 m depth | $3.49\text{ -- }6.56\text{ km/s}$ |
| `crustal_thickness` | Continental crustal thickness | $20.30\text{ -- }54.75\text{ km}$ |
| `dVs_20km` | S-wave velocity anomaly at 20 km depth | $-1.67\text{ -- }8.18\text{ \%}$ |
| `Vp_6000m` | P-wave seismic velocity at 6,000 m depth | $3.49\text{ -- }6.56\text{ km/s}$ |
| `VpVs_60km` | Seismic velocity ratio ($V_p / V_s$) at 60 km depth | $1.72\text{ -- }1.81$ |
| `dVs_60km` | S-wave velocity anomaly at 60 km depth | $-4.57\text{ -- }6.52\text{ \%}$ |
| `gg_mantle_60km` | Geothermal gradient mantle proxy at 60 km depth | $4.51\text{ -- }21.93\text{ }^\circ\text{C/km}$ |
| `dVpVs_60km` | $V_p / V_s$ velocity ratio anomaly at 60 km depth | $-2.58\text{ -- }1.45\text{ \%}$ |
| `dVs_40km` | S-wave velocity anomaly at 40 km depth | $-3.17\text{ -- }8.35\text{ \%}$ |
| `elevation_detrend` | Topographic surface elevation (detrended) | $-789.0\text{ -- }984.0\text{ m}$ |

---

## 📊 Summary of Experimental Results ($N = 200,000$)

| Model Architecture | 5-Fold RMSE (°C) | Disjoint 180k RMSE (°C) | Mean MAE (°C) | Mean $R^2$ (%) | Wilcoxon $p_{\text{Holm}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Multiple Linear Regression (Baseline) | $8.71 \pm 0.07$ | $8.71 \pm 0.07$ | $6.09$ | $68.16\%$ | $< 0.0001$ |
| Random Forest (Default Untuned) | $5.80 \pm 0.07$ | $5.80 \pm 0.07$ | $3.96$ | $85.58\%$ | $< 0.0001$ |
| XGBoost (Default Untuned) | $4.89 \pm 0.07$ | $4.89 \pm 0.07$ | $3.30$ | $89.86\%$ | $< 0.0001$ |
| Random Forest (Optuna Tuned) | $3.72 \pm 0.07$ | $3.72 \pm 0.07$ | $2.27$ | $93.97\%$ | $< 0.0001$ |
| XGBoost (Optuna Tuned) | $3.69 \pm 0.07$ | $3.69 \pm 0.07$ | $2.32$ | $94.16\%$ | $< 0.0001$ |
| Simple Averaging Ensemble (0.5 RF + 0.5 XGB) | $3.57 \pm 0.07$ | $3.57 \pm 0.07$ | $2.21$ | $94.50\%$ | $< 0.0001$ |
| **Hybrid Stacking (Proposed Depth-Specific)** | $\mathbf{3.56 \pm 0.07}$ | $\mathbf{3.57 \pm 0.07}$ | $\mathbf{2.22}$ | $\mathbf{94.53\%}$ | **Reference** |
| **Hybrid Stacking (Cross-Depth Meta-Learner)** | $\mathbf{3.52 \pm 0.07}$ | $\mathbf{3.52 \pm 0.07}$ | $\mathbf{2.19}$ | $\mathbf{94.68\%}$ | $< 0.0001$ |

---

## 📁 Repository Structure

```
geothermal-subsurface-prediction/
├── Revisi_Model.ipynb          # End-to-end Python experimental pipeline & verification
├── app.py                      # Flask backend application serving predictions
├── requirements.txt            # Python dependencies
├── run_app.bat                 # One-click Windows application launcher
├── scaler_geotermal.pkl        # Serialized StandardScaler (855 bytes)
├── static/                     # CSS stylesheets and UI assets
│   ├── dashboard.css
│   ├── login.css
│   └── login.js
├── templates/                  # Frontend HTML templates
│   └── index.html
├── .gitignore                  # Git tracking exclusion rules
└── README.md                   # Project documentation and reproduction guide
```

---

## 🚀 Quickstart: Running the Web Application

### Step 1: Clone Repository
```bash
git clone https://github.com/pranataa-labs/geothermal-subsurface-prediction.git
cd geothermal-subsurface-prediction
```

### Step 2: Download Model Artifacts
Download `model_geotermal_hybrid.pkl` from the **[Google Drive Link](https://drive.google.com/drive/folders/1eAcN74KvVi5Pjj2qIRBgYzUZwVC3m7qV?usp=sharing)** and place it directly inside the root folder:
```
geothermal-subsurface-prediction/
├── model_geotermal_hybrid.pkl   <-- Place downloaded .pkl here
├── scaler_geotermal.pkl
├── app.py
...
```

### Step 3: Set Up Python Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Linux / macOS:
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Launch Web Server
```bash
python app.py
```
*(Alternatively, on Windows you can simply double-click `run_app.bat`)*

Open your web browser and navigate to:  
**`http://127.0.0.1:5000`**

---

## 📓 Running the Experimental Notebook (`Revisi_Model.ipynb`)

To reproduce the complete experimental workflow:
1. Ensure `dataset_200k_with_coords.csv` is downloaded from Google Drive and located in your working directory.
2. Launch Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook Revisi_Model.ipynb
   ```
3. The notebook contains 10 structured sections:
   - §1: Environment configuration and deterministic seed setup (`random_state=42`).
   - §2: Data acquisition and provenance verification on STEM-US.
   - §3: Optuna Bayesian TPE hyperparameter optimization ($N_{\text{tune}} = 20,000$).
   - §4: 5-Fold cross-validation and 9-model ablation study.
   - §5: Depth-stratified error metrics and 95% empirical prediction intervals.
   - §6: Two-sided Wilcoxon signed-rank tests with Holm-Bonferroni correction.
   - §7: Physical consistency analysis and vertical temperature gradient evaluation ($\Delta T / \Delta z$).
   - §8: Spatially blocked cross-validation across regional $K$-means geological clusters.
   - §9: Multi-depth SHAP attribution and Taylor diagram generation.
   - §10: Automatic packaging of verification tables and figures.

---

## 📜 Citation & License

This project is licensed under the MIT License. If you utilize this codebase, models, or methodology in your academic work, please cite:

```bibtex
@article{sastra2026multioutput,
  title={Multi-Output Hybrid Ensemble Application for Predicting Geothermal Subsurface Temperature Profiles},
  author={Sastra, Muhammad Aria and Widiono, Suyud},
  journal={bit-Tech (Binary Computing and Information Technology)},
  year={2026}
}
```
