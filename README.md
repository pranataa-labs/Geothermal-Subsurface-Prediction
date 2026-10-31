# Multi-Output Hybrid Ensemble for Geothermal Subsurface Temperature Profiles

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

> [!IMPORTANT]
> ### 1. Dataset Extraction & Subsampling: [`dataset-splitting.ipynb`](./dataset-splitting.ipynb)
> Extracts the final 101 records (**`101_dataset_testing.csv`**) as an isolated application test set from the raw 534,942-row compilation (`dataset.csv`, sourced from the Stanford Geothermal Data Repository submission #1592 at https://gdr.openei.org/submissions/1592) and draws the uniform random subsample of $N = 200,000$ profiles (**`dataset_200k_with_coords.csv`**, `random_state = 42`) from the remaining 534,841-row primary sampling pool.
>
> ### 2. Core Model Training: [`core-model-training.ipynb`](./core-model-training.ipynb)
> The standalone training pipeline used to train and serialize the final production models (**`model_geotermal_hybrid.pkl`** and **`scaler_geotermal.pkl`**) using optimal hyperparameters on 200,000 samples.
>
> ### 3. Model Testing & Evaluation: [`revised-model-testing.ipynb`](./revised-model-testing.ipynb)
> The comprehensive model evaluation and verification pipeline containing the complete experimental execution, 9-model ablation benchmarks, physical gradient consistency evaluations, spatial block cross-validation, SHAP attributions, and Wilcoxon statistical significance testing.

---

## Repository Structure

```text
geothermal-subsurface-prediction/
├── dataset-splitting.ipynb          # [1. DATA PREP] Extracts 101_dataset_testing.csv & samples dataset_200k_with_coords.csv
├── core-model-training.ipynb        # [2. CORE TRAINING] Standalone training script generating .pkl artifacts
├── revised-model-testing.ipynb      # [3. MODEL TESTING] Comprehensive experimental evaluation & statistical testing pipeline
└── README.md                        # Project documentation
```
