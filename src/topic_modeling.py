import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD, LatentDirichletAllocation
from .topic_utils import custom_stopwords, print_topics

def load_texts(csv_file: str, min_len: int = 5):
    df = pd.read_csv(csv_file)
    texts = df["lemma_text"].astype(str)
    texts = texts[texts.str.split().str.len() > min_len].reset_index(drop=True)
    return texts

def run_lsa(texts, k=5):
    tfidf = TfidfVectorizer(min_df=5, max_df=0.9, stop_words=custom_stopwords)
    X_tfidf = tfidf.fit_transform(texts)
    lsa = TruncatedSVD(n_components=k, random_state=42)
    X_lsa = lsa.fit_transform(X_tfidf)
    topics = print_topics(lsa, tfidf.get_feature_names_out())
    return X_lsa, topics

def run_lda(texts, k=5):
    count_vect = CountVectorizer(min_df=5, max_df=0.9, stop_words=custom_stopwords)
    X_count = count_vect.fit_transform(texts)
    lda = LatentDirichletAllocation(n_components=k, random_state=42)
    X_lda = lda.fit_transform(X_count)
    topics = print_topics(lda, count_vect.get_feature_names_out())
    return X_lda, topics
