# Credit Card Fraud Detection using Sampling Techniques

## 1. Introduction
Credit card fraud detection is a real-world machine learning problem where the dataset is highly imbalanced, with fraudulent transactions forming a very small portion of the total data. Such imbalance can significantly affect model performance.  
This project focuses on balancing the dataset, applying multiple sampling techniques, and evaluating how these techniques influence the accuracy of different machine learning models.

---

## 2. Dataset Description
- **Dataset Name:** Creditcard_data.csv  
- **Source:** GitHub link provided in the assignment  
- **Target Column:** `Class`  
  - `0` → Non-Fraud  
  - `1` → Fraud  
- **Nature of Data:** Highly imbalanced

---

## 3. Development Environment
- **IDE:** Visual Studio Code (VS Code)  
- **Notebook Type:** Jupyter Notebook (`.ipynb`) executed locally  
- **Programming Language:** Python  
- **Libraries Used:**
  - pandas
  - numpy
  - scikit-learn
  - imbalanced-learn
  - matplotlib

> VS Code with Jupyter Notebook support provides functionality equivalent to Google Colab and enables reproducible experiments.

---

## 4. Methodology

### 4.1 Train–Test Split
The dataset is first split into:
- **80% Training data**
- **20% Testing data**

Stratified splitting is used to preserve the class distribution.  
This step is performed **before applying any sampling technique** to prevent data leakage.

---

### 4.2 Handling Class Imbalance
- **Random Oversampling** is applied **only on the training dataset**
- This balances fraud and non-fraud classes
- The test dataset remains untouched to ensure realistic evaluation

---

### 4.3 Sampling Techniques Used
Five probabilistic sampling techniques were applied to the balanced training data:

1. **Simple Random Sampling**  
   Randomly selects samples where each record has equal probability of selection.

2. **Systematic Sampling**  
   Selects every k-th data point from the dataset.

3. **Stratified Sampling**  
   Maintains proportional representation of fraud and non-fraud classes.

4. **Cluster Sampling**  
   Divides the data into clusters and randomly selects one cluster.

5. **Bootstrap Sampling**  
   Sampling with replacement to improve model stability.

---

### 4.4 Machine Learning Models
The following five models were trained and evaluated:

- **M1:** Logistic Regression  
- **M2:** Decision Tree  
- **M3:** Random Forest  
- **M4:** Support Vector Machine  
- **M5:** K-Nearest Neighbors  

---

## 5. Results

### 5.1 Accuracy Comparison Table

| Model | Sampling1 | Sampling2 | Sampling3 | Sampling4 | Sampling5 |
|------|----------|----------|----------|----------|----------|
| **M1 Logistic Regression** | 90.32 | 90.97 | 90.97 | 87.74 | 87.10 |
| **M2 Decision Tree** | 98.71 | 96.77 | 98.71 | 96.13 | 96.77 |
| **M3 Random Forest** | 99.35 | 99.35 | 99.35 | 99.35 | 99.35 |
| **M4 SVM** | 69.03 | 69.03 | 69.03 | 67.10 | 70.97 |
| **M5 KNN** | 96.77 | 95.48 | 96.77 | 90.32 | 96.77 |

---

### 5.2 Result Graph
A bar graph was plotted to visually compare the accuracy of different machine learning models across the five sampling techniques.

**Observations:**
- Random Forest achieves consistently high accuracy across all sampling methods
- Logistic Regression shows stable performance with slight variation
- SVM performance is comparatively lower and sensitive to sampling
- KNN and Decision Tree perform well on balanced data

---

## 6. Discussion
The results indicate that sampling techniques significantly influence model performance.  
Random Forest demonstrates robustness to different sampling methods, while SVM shows sensitivity to data distribution.  
Applying sampling only on training data prevents overfitting and ensures reliable evaluation.




