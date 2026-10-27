# 🌋 Multi-Output Hybrid Ensemble for Geothermal Subsurface Temperature Profiles

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Framework Flask](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Google Drive Artifacts](https://img.shields.io/badge/Google%20Drive-Artifacts%20%26%20Model-orange.svg)](https://drive.google.com/drive/folders/1eAcN74KvVi5Pjj2qIRBgYzUZwVC3m7qV?usp=sharing)

---

> [!IMPORTANT]
> ### 🎯 Model Testing: [`revised-model-testing.ipynb`](./revised-model-testing.ipynb)
> The comprehensive model evaluation and verification pipeline is available directly in **[`revised-model-testing.ipynb`](./revised-model-testing.ipynb)**, containing the complete experimental execution, ablation benchmarks, physical gradient consistency evaluations, spatial validation, and statistical significance testing.
>
> ### ⚙️ Core Model Training: [`core-model-training.ipynb`](./core-model-training.ipynb)
> The standalone training pipeline used to train and serialize the final production models (**`model_geotermal_hybrid.pkl`** and **`scaler_geotermal.pkl`**) using optimal hyperparameters on 200,000 samples.

---

## 📥 Large Artifacts & Dataset Download (Google Drive)

Due to GitHub's 100 MB individual file upload limit, the large serialized machine learning model (`model_geotermal_hybrid.pkl`, ~976 MB), full benchmark dataset (`dataset_200k_with_coords.csv`, ~41 MB), and high-resolution output assets are hosted on Google Drive:

👉 **[Download Project Artifacts on Google Drive](https://drive.google.com/drive/folders/1eAcN74KvVi5Pjj2qIRBgYzUZwVC3m7qV?usp=sharing)**

### 📂 Google Drive Folder Structure (`artikel-revisi`):

```
artikel-revisi/
├── 📁 core-model-website/      # Serialized ML Model Artifacts
│   ├── model_geotermal_hybrid.pkl  (~976 MB, Multi-Output Hybrid Stacking Regressor)
│   └── scaler_geotermal.pkl        (855 B, Fitted StandardScaler)
│
├── 📁 dataset/                 # Benchmark Dataset
│   └── dataset_200k_with_coords.csv (~41.1 MB, Conterminous US multi-physics dataset)
│
├── 📁 image-xlxs/              # Publication Figures & Tables
│   ├── Figure_1_Revised_Architecture.png
│   ├── Figure_5_Revised_Flask_Dashboard.png
│   ├── Output_2_SHAP_Plot_MultiDepth.png
│   ├── Output_3_RMSE_vs_Depth.png
│   ├── Output_4_Taylor_Diagram_MultiDepth.png
│   ├── Tabel_1_Statistik_Distribusi_Variabel.xlsx
│   ├── Tabel_2_Ablation_Study_Summary.xlsx
│   ├── Tabel_3_Performa_Per_Kedalaman_dan_Residual.xlsx
│   ├── Tabel_4_Uji_Statistik_Wilcoxon_Holm_Bonferroni.xlsx
│   ├── Tabel_5_Evaluasi_Gradien_Suhu_Vertikal_dan_Inversi.xlsx
│   ├── Tabel_6_Spatial_Block_Cross_Validation.xlsx
│   ├── Tabel_7_SHAP_dan_Feature_Importance_Multi_Kedalaman.xlsx
│   └── Tabel_Hyperparameter_Optuna.xlsx
│
└── 📁 pelatihan-model/         # Model Training & Testing Notebooks
    ├── ⭐ core-model-training.ipynb    (Model training script to produce .pkl artifacts)
    └── ⭐ revised-model-testing.ipynb  (Comprehensive model evaluation & testing pipeline)
```

---

## 📁 Repository Structure

```
geothermal-subsurface-prediction/
├── ⭐ revised-model-testing.ipynb   # 🎯 [MODEL TESTING] Comprehensive experimental evaluation & statistical testing pipeline
├── ⭐ core-model-training.ipynb     # ⚙️ [CORE TRAINING] Standalone training script generating .pkl artifacts
├── app.py                          # Flask backend application serving predictions
├── requirements.txt                # Python dependencies
├── run_app.bat                     # One-click Windows application launcher
├── scaler_geotermal.pkl            # Serialized StandardScaler (855 bytes)
├── static/                         # CSS stylesheets and UI assets
│   ├── dashboard.css
│   ├── login.css
│   └── login.js
├── templates/                      # Frontend HTML templates
│   └── index.html
├── .gitignore                      # Git tracking exclusion rules
└── README.md                       # Project documentation
```
