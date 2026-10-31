# Multi-Output Hybrid Ensemble for Geothermal Subsurface Temperature Profiles

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Google Drive Artifacts](https://img.shields.io/badge/Google%20Drive-Artifacts%20%26%20Model-orange.svg)](https://drive.google.com/drive/folders/1eAcN74KvVi5Pjj2qIRBgYzUZwVC3m7qV?usp=sharing)

---

> [!IMPORTANT]
> ### 1. Dataset Extraction & Subsampling: [`dataset-splitting.ipynb`](./dataset-splitting.ipynb)
> Extracts the final 101 records (**`101_dataset_testing.csv`**) as an isolated application test set from the raw 534,942-row compilation (`dataset.csv`) and draws the uniform random subsample of $N = 200,000$ profiles (**`dataset_200k_with_coords.csv`**, `random_state = 42`) from the remaining 534,841-row primary sampling pool.
>
> ### 2. Core Model Training: [`core-model-training.ipynb`](./core-model-training.ipynb)
> The standalone training pipeline used to train and serialize the final production models (**`model_geotermal_hybrid.pkl`** and **`scaler_geotermal.pkl`**) using optimal hyperparameters on 200,000 samples.
>
> ### 3. Model Testing & Evaluation: [`revised-model-testing.ipynb`](./revised-model-testing.ipynb)
> The comprehensive model evaluation and verification pipeline containing the complete experimental execution, 9-model ablation benchmarks, physical gradient consistency evaluations, spatial block cross-validation, SHAP attributions, and Wilcoxon statistical significance testing.

---

## Large Artifacts & Dataset Download (Google Drive)

Due to GitHub's 100 MB individual file upload limit, the large serialized machine learning model (`model_geotermal_hybrid.pkl`, ~976 MB), full benchmark datasets (`dataset.csv` and `dataset_200k_with_coords.csv`), and high-resolution publication assets are hosted on Google Drive:

**[Download Project Artifacts on Google Drive](https://drive.google.com/drive/folders/1eAcN74KvVi5Pjj2qIRBgYzUZwVC3m7qV?usp=sharing)**

### Google Drive Folder Structure (`artikel-revisi`):

```text
artikel-revisi/
├── core-model-website/         # Serialized ML Model Artifacts
│   ├── model_geotermal_hybrid.pkl  (~976 MB, Multi-Output Hybrid Stacking Regressor)
│   └── scaler_geotermal.pkl        (855 B, Fitted StandardScaler)
│
├── dataset/                    # Benchmark & Testing Datasets
│   ├── dataset.csv                 (~1.11 GB, Raw 534,942-row Stanford Thermal Earth Model compilation)
│   ├── dataset_200k_with_coords.csv (~41.1 MB, N = 200,000 subsampled multi-physics dataset, random_state=42)
│   └── 101_dataset_testing.csv     (~31.8 KB, Reserved final 101 records for independent application testing)
│
├── image-xlxs/                 # Publication Figures & Tables
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
├── dataset-splitting.ipynb     # [1] Dataset extraction & 200,000-row subsampling notebook
├── core-model-training.ipynb   # [2] Model training notebook generating .pkl artifacts
└── revised-model-testing.ipynb # [3] Comprehensive model evaluation & testing pipeline
```

---

## Repository Structure

```text
geothermal-subsurface-prediction/
├── dataset-splitting.ipynb          # [1. DATA PREP] Extracts 101_dataset_testing.csv & samples dataset_200k_with_coords.csv
├── core-model-training.ipynb        # [2. CORE TRAINING] Standalone training script generating .pkl artifacts
├── revised-model-testing.ipynb      # [3. MODEL TESTING] Comprehensive experimental evaluation & statistical testing pipeline
└── README.md                        # Project documentation
```
