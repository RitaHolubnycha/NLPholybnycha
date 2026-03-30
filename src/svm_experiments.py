from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, f1_score


def run_svm_word(train_df, val_df, test_df):
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

    model = LinearSVC(C=1.0)
    model.fit(X_train_vec, y_train)

    y_val_pred = model.predict(X_val_vec)
    y_test_pred = model.predict(X_test_vec)

    return accuracy_score(y_val, y_val_pred), f1_score(y_val, y_val_pred, average='macro')


def run_svm_char(train_df, val_df, test_df):
    X_train = train_df['token'] + " " + train_df['lemma']
    X_val = val_df['token'] + " " + val_df['lemma']
    X_test = test_df['token'] + " " + test_df['lemma']

    y_train = train_df['upos']
    y_val = val_df['upos']
    y_test = test_df['upos']

    vectorizer = TfidfVectorizer(
        analyzer='char',
        ngram_range=(3,5),
        sublinear_tf=True
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_val_vec = vectorizer.transform(X_val)
    X_test_vec = vectorizer.transform(X_test)

    model = LinearSVC(C=1.0)
    model.fit(X_train_vec, y_train)

    y_val_pred = model.predict(X_val_vec)
    y_test_pred = model.predict(X_test_vec)

    return accuracy_score(y_val, y_val_pred), f1_score(y_val, y_val_pred, average='macro')


def run_svm_char_balanced(train_df, val_df, test_df):
    X_train = train_df['token'] + " " + train_df['lemma']
    X_val = val_df['token'] + " " + val_df['lemma']
    X_test = test_df['token'] + " " + test_df['lemma']

    y_train = train_df['upos']
    y_val = val_df['upos']
    y_test = test_df['upos']

    vectorizer = TfidfVectorizer(
        analyzer='char',
        ngram_range=(3,5),
        sublinear_tf=True
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_val_vec = vectorizer.transform(X_val)
    X_test_vec = vectorizer.transform(X_test)

    model = LinearSVC(C=1.0, class_weight='balanced')
    model.fit(X_train_vec, y_train)

    y_val_pred = model.predict(X_val_vec)

    return accuracy_score(y_val, y_val_pred), f1_score(y_val, y_val_pred, average='macro')
