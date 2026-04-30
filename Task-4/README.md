# CODTECH Internship Tasks

This repository contains three tasks completed as part of the CODTECH internship program:

1. **Big Data Analytics with PySpark** – Exploratory data analysis on an online retail dataset.
2. **Machine Learning with Scikit-learn** – Classification on the breast cancer dataset.
3. **Interactive Web Application with Streamlit** – A simple web app to interact with the trained ML model.

---

## 📁 Repository Structure

```
.
├── data.csv                     # Retail dataset for Task 1
├── main_task1.ipynb             # PySpark retail analysis notebook
├── main_task2.ipynb             # Scikit-learn breast cancer notebook
├── main_task3.ipynb             # Streamlit setup (placeholder)
├── app.py                       # Streamlit web application (Task 3)
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

> **Note:** The notebook files are named `main.ipynb` in the original submission; they have been renamed here for clarity.

---

## ✅ Task 1 – Big Data Analytics with PySpark

**Objective:**  
Analyze an online retail dataset using PySpark to extract insights such as top revenue‑generating countries and best‑selling products.

**Dataset:**  
`data.csv` – Contains transactional data with fields like `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`.  
*(Assumed to be the UCI Online Retail dataset)*

**Key Steps:**
1. Load and inspect raw data.
2. Clean data: remove rows with null `CustomerID` and negative `Quantity`.
3. Create a `TotalAmount` column (`Quantity * UnitPrice`).
4. Compute top 10 countries by revenue.
5. Compute top 10 best‑selling products.
6. Visualize results using Matplotlib.

**Run the notebook:**
```bash
jupyter notebook main_task1.ipynb
```

**Dependencies:** See `requirements.txt`.

---

## ✅ Task 2 – Machine Learning with Scikit‑learn

**Objective:**  
Build a classification model to predict breast cancer (malignant / benign) using the Wisconsin Breast Cancer dataset.

**Key Steps:**
1. Load dataset from `sklearn.datasets.load_breast_cancer`.
2. Select top 10 features using `SelectKBest` with ANOVA F‑test.
3. Split data into training and testing sets.
4. Scale features using `StandardScaler`.
5. Train a `LogisticRegression` classifier.
6. Evaluate using accuracy, confusion matrix, and classification report.

**Run the notebook:**
```bash
jupyter notebook main_task2.ipynb
```

---

## ✅ Task 3 – Interactive Web App with Streamlit

**Objective:**  
Create a simple web application that allows users to input feature values and obtain a cancer prediction from the trained model.

**Implementation:**
- A basic Streamlit app (`app.py`) that:
  - Loads the pre‑trained logistic regression model and scaler (saved from Task 2).
  - Provides numeric input fields for the 10 selected features.
  - Displays the prediction (Malignant / Benign) and probability.

**How to use:**
1. Train and save the model from Task 2 by adding the following code at the end of the notebook:
   ```python
   import joblib
   joblib.dump(model, 'cancer_model.pkl')
   joblib.dump(scaler, 'scaler.pkl')
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

**Note:** If the model files are not present, the app will display an error message. A placeholder script is provided; you need to generate the model first.

---

## ⚙️ Installation

1. **Clone the repository** (or extract the provided files).

2. **Set up a Python virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Java for PySpark**  
   PySpark requires Java (version 8 or 11). If you are using **Java 21**, you must add the following JVM option to avoid the `SecurityManager` issue (already included in the notebook):
   ```python
   os.environ['PYSPARK_SUBMIT_ARGS'] = '--driver-java-options "-Djava.security.manager=allow" pyspark-shell'
   ```

5. **Launch Jupyter Notebook** (for Tasks 1 & 2):
   ```bash
   jupyter notebook
   ```

---

## 📊 Dataset Notes

- **Task 1** expects a file named `data.csv` in the same directory. If you are using a different file, update the path in the notebook.
- **Task 2** uses the built‑in breast cancer dataset from scikit‑learn – no external download required.

---

## 📝 License

This project is for educational purposes as part of the CODTECH internship.

---

## 🙋‍♂️ Author

[Your Name] – [Your Email]  
*Intern at CODTECH*