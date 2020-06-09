from natasha import (
     Segmenter,
     MorphVocab,

     NewsEmbedding,
     NewsMorphTagger,
     NewsSyntaxParser,
     NewsNERTagger,

     PER,
     NamesExtractor,
     Doc
     )


class NER(object):
    def __init__(self):
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        self.emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(self.emb)
        self.syntax_parser = NewsSyntaxParser(self.emb)
        self.ner_tagger = NewsNERTagger(self.emb)
        self.names_extractor = NamesExtractor(self.morph_vocab)

    def __call__(self, text):
        doc = Doc(text)
        doc.segment(self.segmenter)
        doc.tag_ner(self.ner_tagger)

        ner = []
        for span in doc.spans:
            ner.append(span.text)
        #print(ner)
        return ner