# ☄️ Intelligent Near-Earth Object Hazard Prediction Using Machine Learning

A comprehensive Machine Learning project that predicts whether a **Near-Earth Object (NEO)** is **Hazardous** or **Non-Hazardous** using NASA's historical asteroid dataset.

This project demonstrates a complete end-to-end Machine Learning pipeline, including **Data Preprocessing, Exploratory Data Analysis (EDA), Feature Engineering, Model Development, Explainable AI (XAI), and Deployment using Streamlit**.

---

## 📌 Project Overview

Near-Earth Objects (NEOs) are asteroids and comets whose orbits bring them close to Earth's orbital path. While most of these objects are harmless, some are classified as **Potentially Hazardous Asteroids (PHAs)** due to their size and proximity to Earth.

The increasing number of asteroid observations makes manual hazard identification challenging. This project leverages Machine Learning techniques to automate the prediction of asteroid hazard status based on physical and orbital characteristics.

---

## 🎯 Objectives

- Predict whether a Near-Earth Object is hazardous or non-hazardous.
- Perform comprehensive data preprocessing and cleaning.
- Conduct Exploratory Data Analysis (EDA).
- Apply feature engineering techniques.
- Handle class imbalance using SMOTE.
- Train and compare multiple Machine Learning models.
- Evaluate model performance using standard classification metrics.
- Explain predictions using Explainable AI (Feature Importance & SHAP).
- Deploy the trained model using Streamlit.

---

## 📂 Dataset Information

**Dataset:** NASA Near-Earth Object (NEO) Dataset

### Features Used

| Feature | Description |
|----------|-------------|
| est_diameter_min | Estimated Minimum Diameter |
| est_diameter_max | Estimated Maximum Diameter |
| relative_velocity | Relative Velocity |
| miss_distance | Closest Distance from Earth |
| orbiting_body | Orbiting Celestial Body |
| sentry_object | NASA Sentry Monitoring Flag |
| absolute_magnitude | Brightness of Asteroid |
| hazardous | Target Variable |

---

## ⚙️ Project Workflow

```text
Dataset Collection
        │
        ▼
Data Preprocessing
        │
        ▼
Exploratory Data Analysis (EDA)
        │
        ▼
Feature Engineering
        │
        ▼
Feature Scaling
        │
        ▼
Train-Test Split
        │
        ▼
SMOTE Oversampling
        │
        ▼
Machine Learning Models
        │
        ▼
Model Evaluation
        │
        ▼
Explainable AI (SHAP)
        │
        ▼
Streamlit Deployment
```

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Dataset Inspection
- Missing Value Analysis
- Duplicate Record Detection
- Class Distribution
- Histograms
- Boxplots
- Correlation Heatmap
- Feature Relationship Analysis

---

## 🤖 Machine Learning Models Implemented

The following supervised Machine Learning algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- XGBoost Classifier

---

## 📈 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|---------:|----------:|--------:|----------:|---------:|
| Logistic Regression | 78.62% | 0.304 | 0.932 | 0.459 | 0.879 |
| Decision Tree | 89.27% | 0.459 | 0.574 | 0.510 | 0.750 |
| ⭐ Random Forest | **89.92%** | **0.486** | **0.617** | **0.544** | **0.930** |
| Gradient Boosting | 79.66% | 0.322 | 0.984 | 0.485 | 0.916 |
| XGBoost | 84.48% | 0.361 | 0.775 | 0.493 | 0.918 |

**Best Performing Model:** Random Forest Classifier

---

## 🔍 Explainable AI (XAI)

To improve model transparency and interpretability, the following Explainable AI techniques were implemented:

- Feature Importance Analysis
- SHAP (SHapley Additive Explanations)

These techniques help identify the most influential features contributing to asteroid hazard prediction.

---

## 🌐 Streamlit Web Application

A user-friendly Streamlit application was developed to demonstrate real-time predictions.

Users can enter asteroid characteristics such as:

- Estimated Minimum Diameter
- Relative Velocity
- Miss Distance
- Absolute Magnitude

The application predicts whether the asteroid is:

- ⚠️ Hazardous
- ✅ Non-Hazardous

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries & Frameworks

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

## 📁 Repository Structure

```text
Asteroid-prediction-using-machine-learning/
│
├── Intelligent_Near_Earth_Object_Hazard_Prediction_Using_Machine_Learning.ipynb
├── Project_Report.pdf
├── app.py
├── asteroid_model.pkl
├── scaler.pkl
├── requirements.txt
├── neo.csv
├── README.md
└── screenshots/
```

---

## 🚀 Installation Guide

### Clone the Repository

```bash
git clone https://github.com/your-github-username/Asteroid-prediction-using-machine-learning.git
```

### Navigate to the Project Directory

```bash
cd Asteroid-prediction-using-machine-learning
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 📷 Project Screenshots

Add screenshots of the following outputs inside the `screenshots` folder:

- Dataset Preview
- Class Distribution
- Correlation Heatmap
- Model Comparison
- Confusion Matrix
- Feature Importance
- SHAP Summary Plot
- Streamlit Home Page
- Prediction Result

---

## 📌 Future Scope

- Integration with NASA Live NEO API
- Cloud Deployment using Streamlit Community Cloud
- Real-Time Asteroid Monitoring
- Advanced Deep Learning Models
- Automated Alert System
- Interactive Dashboard for Astronomical Analysis

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

B.Tech – Computer Science & Engineering (Cyber Security)

Machine Learning | Data Science | Artificial Intelligence

📧 **Email:** khwajachisty876@gmail.com
