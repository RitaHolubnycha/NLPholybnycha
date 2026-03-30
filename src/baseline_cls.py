from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score


def run_logreg_baseline(train_df, val_df, test_df):
    X_train = train_df['token'] + " " + train_df['lemma']
    X_val = val_df['token'] + " " + val_df['lemma']
    X_test = test_df['token'] + " " + test_df['lemma']

    y_train = train_df['upos']
    y_val = val_df['upos']
    y_test = test_df['upos']

    vectorizer = TfidfVectorizer(
        analyzer='word',
        ngram_range=(1,2),
        sublinear_tf=True
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_val_vec = vectorizer.transform(X_val)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train_vec, y_train)

    y_val_pred = model.predict(X_val_vec)
    y_test_pred = model.predict(X_test_vec)

    return {
        "val_acc": accuracy_score(y_val, y_val_pred),
        "val_f1": f1_score(y_val, y_val_pred, average='macro'),
        "test_acc": accuracy_score(y_test, y_test_pred),
        "test_f1": f1_score(y_test, y_test_pred, average='macro')
    }
