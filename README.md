# AI : LAB 1 - KNN Classification & Deployment

This repository contains two machine learning projects focused on the K-Nearest Neighbors (KNN) algorithm and its deployment using Streamlit.

## Projects Overview

### 1. IRIS Flower Classification
A machine learning model that predicts the species of an Iris flower based on its morphological features.

*   **Location:** Root directory
*   **Dataset:** `iris.csv` (features: sepal length, sepal width, petal length, petal width)
*   **Technique:** KNN (K-Nearest Neighbors)
*   **Deployment:** Streamlit Dashboard
*   **Live Demo:** [irisknn.streamlit.app](https://irisknn.streamlit.app/)

### 2. Weight Classification (Assignment)
A practical implementation to classify individuals into health categories based on their height and weight.

*   **Location:** `/assignment`
*   **Dataset:** `height_weight_knn.csv` (features: height in cm, weight in kg)
*   **Technique:** KNN (K-Nearest Neighbors)
*   **Deployment:** Streamlit Dashboard
*   **Live Demo:** [heightweightknn.streamlit.app](https://heightweightknn.streamlit.app/)

---

## 🛠️ Setup & Installation

Ensure you have Python installed. It is recommended to use a virtual environment.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Lab1
    ```

2.  **Install dependencies:**
    If you use `uv`:
    ```bash
    uv sync
    ```
    Or using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Dependencies include `streamlit`, `scikit-learn`, `pandas`, `numpy`, and `joblib`)*

---

## 🚀 Running the Applications

### 🌸 Iris Flower Classifier
To launch the Iris classification app:
```bash
streamlit run deploy.py
```

### ⚖️ Weight Classifier (Assignment)
To launch the height-weight analysis app:
```bash
cd assignment
streamlit run deploy.py
```

---

## 📂 Project Structure

```text
Lab1/
├── assignment/               # Weight Classification Project
│   ├── deploy.py             # Streamlit deployment script
│   ├── home.ipynb            # Model training & EDA
│   ├── height_weight_knn.csv # Dataset
│   └── model.joblib          # Trained KNN model
├── iris.csv                  # Iris dataset
├── lab1.ipynb                # Iris model training & EDA
├── deploy.py                 # Iris Streamlit deployment script
├── model.joblib              # Trained Iris mockup model
├── pyproject.toml            # Project configuration
└── README.md                 # Project documentation
```

---

## 📊 Visualizations
The projects include various plots generated during testing, such as:
- Confusion Matrices
- Feature Distributions
- Scatter Plots for KNN visualization