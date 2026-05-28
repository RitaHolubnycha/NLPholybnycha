# =========================
# 1. Imports
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score, f1_score, classification_report,
    confusion_matrix, ConfusionMatrixDisplay,
    precision_recall_curve, auc
)

# =========================
# 2. Data loading
# =========================
from google.colab import files
uploaded = files.upload()

train_df = pd.read_csv("train.csv")
val_df   = pd.read_csv("validation.csv")
test_df  = pd.read_csv("test.csv")

# =========================
# 3. Feature preparation
# =========================

# baseline text (token only)
train_df["text"] = train_df["token"].astype(str)
val_df["text"]   = val_df["token"].astype(str)
test_df["text"]  = test_df["token"].astype(str)

# improved text (token + lemma)
train_df["text2"] = train_df["token"] + " " + train_df["lemma"]
val_df["text2"]   = val_df["token"] + " " + val_df["lemma"]
test_df["text2"]  = test_df["token"] + " " + test_df["lemma"]

# =========================
# 4. Model 1 — Logistic Regression baseline
# =========================
pipe1 = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,1))),
    ("clf", LogisticRegression(max_iter=300))
])

pipe1.fit(train_df["text"], train_df["upos"])

# =========================
# 5. Model 2 — Logistic Regression (bigger features)
# =========================
pipe2 = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), sublinear_tf=True)),
    ("clf", LogisticRegression(max_iter=500))
])

pipe2.fit(train_df["text2"], train_df["upos"])

# =========================
# 6. Predictions
# =========================
pred1 = pipe1.predict(test_df["text"])
pred2 = pipe2.predict(test_df["text2"])

# =========================
# 7. Evaluation
# =========================
print("=== BASELINE 1 ===")
print("Accuracy:", accuracy_score(test_df["upos"], pred1))
print("Macro-F1:", f1_score(test_df["upos"], pred1, average="macro"))

print("\n=== BASELINE 2 ===")
print("Accuracy:", accuracy_score(test_df["upos"], pred2))
print("Macro-F1:", f1_score(test_df["upos"], pred2, average="macro"))

print("\nClassification report:")
print(classification_report(test_df["upos"], pred2))

# =========================
# 8. Confusion matrix
# =========================
ConfusionMatrixDisplay.from_predictions(
    test_df["upos"], pred1
)
plt.show()

ConfusionMatrixDisplay.from_predictions(
    test_df["upos"], pred2
)
plt.show()

# =========================
# 9. Feature importance (LinearSVC-style analysis)
# =========================
vectorizer = pipe2.named_steps["tfidf"]
clf = pipe2.named_steps["clf"]

feature_names = np.array(vectorizer.get_feature_names_out())
classes = clf.classes_

for i, cls in enumerate(classes):
    top10 = np.argsort(clf.coef_[i])[-10:]
    print(f"\nTop features for {cls}:")
    print(feature_names[top10])

# =========================
# 10. Error analysis
# =========================
errors = test_df.copy()
errors["pred"] = pred2

errors = errors[errors["upos"] != errors["pred"]]

print("Кількість помилок:", len(errors))
print(errors[["token", "lemma", "upos", "pred"]].head(10))
