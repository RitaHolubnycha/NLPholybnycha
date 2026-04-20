from gensim.models import Word2Vec, FastText

def train_word2vec(sentences, vector_size=100, window=5, min_count=3, sg=1):
    model = Word2Vec(
        sentences=sentences,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        sg=sg
    )
    model.build_vocab(sentences)
    model.train(sentences, total_examples=len(sentences), epochs=10)
    return model


def train_fasttext(sentences, vector_size=100, window=5, min_count=3, sg=1):
    model = FastText(
        sentences=sentences,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        sg=sg
    )
    model.build_vocab(sentences)
    model.train(sentences, total_examples=len(sentences), epochs=10)
    return model
