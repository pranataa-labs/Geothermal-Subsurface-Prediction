# 🌋 Multi-Output Hybrid Ensemble for Geothermal Subsurface Temperature Profiles

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Framework Flask](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Google Drive Artifacts](https://img.shields.io/badge/Google%20Drive-Artifacts%20%26%20Model-orange.svg)](https://drive.google.com/drive/folders/1eAcN74KvVi5Pjj2qIRBgYzUZwVC3m7qV?usp=sharing)

---

> [!IMPORTANT]
> ### 🎯 Primary Reviewer Deliverable: [`Revisi_Model.ipynb`](./Revisi_Model.ipynb)
> The primary experimental notebook requested by the peer reviewers is available directly in the root of this repository: **[`Revisi_Model.ipynb`](./Revisi_Model.ipynb)**.  
> It provides the full, reproducible Python execution pipeline and numerical outputs covering:
> 1. **Optuna Bayesian TPE Hyperparameter Tuning** ($N_{\text{tune}} = 20,000$ independent partition).
> 2. **9-Model Ablation Study & 5-Fold Cross-Validation** ($N = 200,000$ benchmark and disjoint $N = 180,000$).
> 3. **Paired Wilcoxon Signed-Rank Statistical Tests** with Holm-Bonferroni correction and rank-biserial effect sizes ($r_{\text{rb}}$).
> 4. **Physical Gradient Consistency** ($\Delta T / \Delta z$) and zero-inversion verification ($0.0000\%$ violation rate).
> 5. **Spatial Block Cross-Validation** across geographically disjoint regional geological clusters.
> 6. **Multi-Depth SHAP Attribution** and multi-depth Taylor diagram evaluation.

---

## 📥 Reviewer Resources & Large Artifacts Download (Google Drive)

Due to GitHub's 100 MB individual file upload limit, the large serialized machine learning model (`model_geotermal_hybrid.pkl`, ~976 MB), full benchmark dataset (`dataset_200k_with_coords.csv`, ~41 MB), and high-resolution output assets are hosted on Google Drive:

👉 **[Download Reviewer Artifacts on Google Drive](https://drive.google.com/drive/folders/1eAcN74KvVi5Pjj2qIRBgYzUZwVC3m7qV?usp=sharing)**

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
└── 📁 pelatihan-model/         # Experimental Training Notebook
    └── ⭐ Revisi_Model.ipynb       (Primary reviewer notebook mirror)
```

---

## 📁 Repository Structure

```
geothermal-subsurface-prediction/
├── ⭐ Revisi_Model.ipynb       # 🎯 [PRIMARY REVIEWER NOTEBOOK] Complete experimental & statistical validation pipeline
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
└── README.md                   # Project documentation
```
