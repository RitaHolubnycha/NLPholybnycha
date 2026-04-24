import spacy

class NERPipeline:
    def __init__(self, model_name="uk_core_news_sm"):
        self.nlp = spacy.load(model_name)

    def extract(self, text):
        """
        Базовий spaCy NER
        """
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]

    def extract_batch(self, texts):
        return [self.extract(t) for t in texts]
