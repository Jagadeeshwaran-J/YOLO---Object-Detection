# 📊 Evaluation Metrics Explained (with Formulas & Examples)

When evaluating an object detection or classification model, it’s crucial to understand metrics like **Precision**, **Recall**, **Accuracy**, and **F1 Score**. Here's a simple breakdown:

---

## 🎯 1. Precision – *How many predicted positives were actually correct?*

> “Out of all the objects you predicted as positive, how many are truly positive?”

**Formula:**
```ini
Precision = TP / (TP + FP)
```

**Example:**

- Model predicted 10 objects as positive  
- Actual positives among those: 7  
- → **Precision = 7 / 10 = 0.70 (or 70%)**

---

## 📥 2. Recall – *How many actual positives were correctly predicted?*

> “Out of all the actual positive objects, how many did you find?”

**Formula:**
```ini
Recall = TP / (TP + FN)
```

**Example:**

- Total actual positive objects = 10  
- Model correctly predicted 7 of them  
- → **Recall = 7 / 10 = 0.70 (or 70%)**

---

## 📌 3. Accuracy – *How many predictions were correct overall?*

> “Out of all predictions, how many are right?”

**Formula:**
```ini
Accuracy = (TP + TN) / (TP + FP + FN + TN)
```

**Example:**

- TP = 7, FP = 3, FN = 3, TN = 87  
- → **Accuracy = (7 + 87) / (7 + 3 + 3 + 87) = 94 / 100 = 94%**

---

## ⚖️ 4. F1 Score – *The harmonic mean of precision and recall*

> “Balance between precision and recall. High only when both are high.”

**Formula:**
```sql
F1 Score = 2 × (Precision × Recall) / (Precision + Recall)
```

**Example:**

- Precision = 0.70  
- Recall = 0.70  
- → **F1 Score = 2 × (0.7 × 0.7) / (0.7 + 0.7) = 0.70**

---

## 📋 Summary Table

| Metric     | Formula                               | Description                              |
|------------|----------------------------------------|------------------------------------------|
| Precision  | `TP / (TP + FP)`                      | How accurate are positive predictions    |
| Recall     | `TP / (TP + FN)`                      | How well the model finds actual positives|
| F1 Score   | `2 × (P × R) / (P + R)`               | Balance of Precision & Recall            |
| Accuracy   | `(TP + TN) / (TP + FP + FN + TN)`     | Overall correctness                      |

---

## 🔍 So, when is a model good?

| Metric     | Ideal Value (Rule of Thumb)          |
|------------|---------------------------------------|
| Precision  | ≥ 0.80 (80%) – good; > 0.90 – excellent |
| Recall     | ≥ 0.80 – good; > 0.90 – excellent       |
| F1 Score   | ≥ 0.80 – good; > 0.90 – excellent       |
| Accuracy   | ≥ 0.90 – good, *only if* data is balanced |

---

## ✅ Final Takeaway

- A **good model** has **high precision, recall, F1 score, and accuracy**.
- A **bad model** might have **high accuracy** but **low precision/recall** (especially on imbalanced data).
- Always look at **F1 score** for the most reliable summary of model performance.

