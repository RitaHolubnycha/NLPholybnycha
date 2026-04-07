import numpy as np

custom_stopwords = [
    "це", "що", "як", "так", "не", "до", "на", "за",
    "ви", "ми", "вони", "цей", "той",
    "шановний", "колега", "депутат",
    "про", "питання", "увага", "будь", "ласка", "народний", "дякувати", "слово", "прошу",
    "фракція", "рада", "україна", "який", "бути"
]

def print_topics(model, feature_names, n_top_words=10):
    topics = []
    for i, comp in enumerate(model.components_):
        words = [feature_names[j] for j in comp.argsort()[-n_top_words:][::-1]]
        topic_str = f"Topic {i}: {' '.join(words)}"
        print(topic_str)
        topics.append(words)
    return topics

def get_top_docs(X_topics, texts, topic_idx, top_n=2):
    idx = np.argsort(X_topics[:, topic_idx])[::-1][:top_n]
    return texts.iloc[idx].values
