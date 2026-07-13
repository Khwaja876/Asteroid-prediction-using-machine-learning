# ☄️ Project Sentinel: Hazardous Asteroid Prediction AI

An end-to-end Machine Learning project that predicts whether a **Near-Earth Object (NEO)** is **Hazardous** or **Non-Hazardous** using NASA's asteroid dataset.

The project demonstrates the complete machine learning pipeline, including **data preprocessing, exploratory data analysis (EDA), feature engineering, model development, explainable AI, and deployment using Streamlit**.

---

## 📌 Project Overview

Near-Earth Objects (NEOs) are asteroids and comets whose orbits bring them close to Earth. While many of these objects pose no immediate threat, some are classified as **Potentially Hazardous Asteroids (PHAs)** due to their size and proximity to Earth.

This project develops a supervised machine learning model capable of predicting asteroid hazard status based on historical observations from NASA's Near-Earth Object dataset.

---

## 🎯 Objectives

- Predict whether an asteroid is hazardous or non-hazardous.
- Perform comprehensive data preprocessing and cleaning.
- Conduct Exploratory Data Analysis (EDA).
- Apply feature engineering techniques.
- Handle class imbalance using SMOTE.
- Train and compare multiple machine learning models.
- Interpret predictions using Explainable AI (SHAP & Feature Importance).
- Deploy the trained model using Streamlit.

---

## 📂 Dataset

**Source:** NASA Near-Earth Object (NEO) Dataset

### Features Used

| Feature | Description |
|----------|-------------|
| est_diameter_min | Estimated minimum diameter |
| est_diameter_max | Estimated maximum diameter |
| relative_velocity | Relative velocity of asteroid |
| miss_distance | Closest distance from Earth |
| orbiting_body | Orbiting celestial body |
| sentry_object | NASA Sentry monitoring flag |
| absolute_magnitude | Asteroid brightness |
| hazardous | Target variable |

---

## ⚙️ Machine Learning Workflow

```
Dataset Collection
        │
        ▼
Data Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Data Scaling
        │
        ▼
Train-Test Split
        │
        ▼
SMOTE Oversampling
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Explainable AI
        │
        ▼
Streamlit Deployment
```

---

## 📊 Exploratory Data Analysis

The dataset was analyzed using multiple visualization techniques:

- Class Distribution
- Histograms
- Boxplots
- Correlation Heatmap
- Feature Relationship Analysis

---

## 🤖 Machine Learning Models

The following classification models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

---

## 📈 Model Performance

| Model | Accuracy | ROC-AUC |
|--------|---------:|---------:|
| Logistic Regression | 78.62% | 0.879 |
| Decision Tree | 89.27% | 0.750 |
| ⭐ Random Forest | **89.92%** | **0.930** |
| Gradient Boosting | 79.66% | 0.916 |
| XGBoost | 84.48% | 0.918 |

**Best Model:** Random Forest Classifier

---

## 🔍 Explainable AI

To improve model interpretability, the following explainability techniques were implemented:

- Feature Importance
- SHAP (SHapley Additive Explanations)

These methods provide insight into how different asteroid characteristics influence the model's predictions.

---

## 🌐 Streamlit Web Application

The trained model was deployed using **Streamlit**.

Users can enter asteroid characteristics and receive real-time predictions indicating whether the asteroid is:

- ⚠️ Hazardous Asteroid
- ✅ Non-Hazardous Asteroid

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- Joblib
- Streamlit
- Imbalanced-learn (SMOTE)

---

## 📁 Project Structure

```
Project-Sentinel/
│
├── Hazardous_Asteroid_Prediction.ipynb
├── app.py
├── asteroid_model.pkl
├── scaler.pkl
├── requirements.txt
├── neo.csv
├── Project_Report.pdf
├── README.md
└── screenshots/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Project-Sentinel.git
```

Move into the project directory

```bash
cd Project-Sentinel
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📷 Project Screenshots

Add the following screenshots to the **screenshots/** folder:

- Dataset Preview
- EDA Visualizations
- Correlation Heatmap
- Model Comparison
- Confusion Matrix
- Feature Importance
- SHAP Summary Plot
- Streamlit Interface

---

## 📌 Future Improvements

- Live NASA API Integration
- Cloud Deployment
- Deep Learning Models
- Real-Time Asteroid Monitoring
- Automated Alert System
- Interactive Dashboard

---

## 📚 References

- NASA Near-Earth Object Dataset
- Scikit-learn Documentation
- XGBoost Documentation
- SHAP Documentation
- Streamlit Documentation

---

## 👨‍💻 Author

**Mohammad Khwaja Moinuddin Chisty**

B.Tech Computer Science & Engineering (Cyber Security)

Machine Learning | Data Science | Artificial Intelligence

---

## ⭐ If you found this project useful, consider giving it a Star!
