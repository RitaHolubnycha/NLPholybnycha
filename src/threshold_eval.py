import numpy as np
from sklearn.preprocessing import label_binarize
from sklearn.metrics import precision_recall_curve, auc


def compute_punct_threshold(model, X_val, y_train, y_val):
    classes = y_train.unique()

    y_val_bin = label_binarize(y_val, classes=classes)
    punct_idx = list(classes).index('PUNCT')

    scores_val = model.decision_function(X_val)
    punct_scores = scores_val[:, punct_idx]
    punct_true = y_val_bin[:, punct_idx]

    precision, recall, thresholds = precision_recall_curve(punct_true, punct_scores)
    auc_pr = auc(recall, precision)

    thresh_idx = np.argmax(precision + recall)
    best_threshold = thresholds[thresh_idx]

    return best_threshold, auc_pr
