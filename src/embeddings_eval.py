def get_neighbors(model, word, topn=10):
    return model.wv.most_similar(word, topn=topn)


def analyze_words(model, words):
    results = {}
    for w in words:
        if w in model.wv:
            results[w] = get_neighbors(model, w)
        else:
            results[w] = None
    return results
