from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    NamesExtractor,
    Doc)

from rutermextract import TermExtractor

class Tokenizer(object):
    def __init__(self):
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        self.emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(self.emb)
        self.syntax_parser = NewsSyntaxParser(self.emb)
        self.ner_tagger = NewsNERTagger(self.emb)
        self.names_extractor = NamesExtractor(self.morph_vocab)
        self.doc = []
        self.term_extractor = TermExtractor()

    def init_doc(self, text):
        self.doc = Doc(text)
        self.doc.segment(self.segmenter)
        self.doc.tag_ner(self.ner_tagger)

    def get_sentance(self, text):
        self.init_doc(text)
        sentences = []
        for sentence in self.doc.sents:
            sentences.append(sentence.text)
        return sentences

    def get_tokens(self, sentence):
        tokens = []
        for term in self.term_extractor(sentence):
            tokens.append(term.normalized)
        return tokens