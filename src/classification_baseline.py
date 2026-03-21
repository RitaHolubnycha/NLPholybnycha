# базовий текст (тільки токен)
train_df["text"] = train_df["token"].astype(str)
val_df["text"]   = val_df["token"].astype(str)
test_df["text"]  = test_df["token"].astype(str)

# покращений текст (token + lemma)
train_df["text2"] = train_df["token"] + " " + train_df["lemma"]
val_df["text2"]   = val_df["token"] + " " + val_df["lemma"]
test_df["text2"]  = test_df["token"] + " " + test_df["lemma"]
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

pipe1 = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,1))),
    ("clf", LogisticRegression(max_iter=300))
])

pipe1.fit(train_df["text"], train_df["upos"])
pipe2 = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), sublinear_tf=True)),
    ("clf", LogisticRegression(max_iter=500))
])

pipe2.fit(train_df["text2"], train_df["upos"])
from sklearn.metrics import accuracy_score, f1_score, classification_report

# baseline 1
pred1 = pipe1.predict(test_df["text"])

print("=== BASELINE 1 ===")
print("Accuracy:", accuracy_score(test_df["upos"], pred1))
print("Macro-F1:", f1_score(test_df["upos"], pred1, average="macro"))

# baseline 2
pred2 = pipe2.predict(test_df["text2"])

print("\n=== BASELINE 2 ===")
print("Accuracy:", accuracy_score(test_df["upos"], pred2))
print("Macro-F1:", f1_score(test_df["upos"], pred2, average="macro"))

print("\nClassification report:")
print(classification_report(test_df["upos"], pred2))
