
Lab7 - LinearSVC + Char-ngrams + Imbalance

Task: POS tagging (token classification)
Baseline Lab6: TF-IDF word(1,2) + Logistic Regression
SVM models tested:
 - LinearSVC Word(1,2)
 - LinearSVC Word+Char(3-5)
 - LinearSVC Word+Char + class_weight='balanced'

Best result (Validation):
 - Accuracy: 0.9712
 - Macro-F1: 0.8364

Char-ngrams helped: Yes
Class_weight='balanced' helped: Yes
Threshold for PUNCT selected: -1.0001
Most frequent errors: short tokens, noisy tokens, class overlap (ADJ/PROPN)
