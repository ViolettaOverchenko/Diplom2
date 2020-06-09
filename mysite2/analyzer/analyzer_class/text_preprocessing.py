from analyzer.analyzer_class.cleaner import Cleaner
from analyzer.analyzer_class.tokenizer import Tokenizer
from analyzer.analyzer_class.abbreviations import Abbreviations


class TextPreprocessing(object):
    def __init__(self):
        self.cleaner = Cleaner()
        self.tokenizer = Tokenizer()
        self.abbreviations = Abbreviations()

    def __call__(self, text):
        sentences = self.tokenizer.get_sentance(text)
        sentences_tokens = []
        for sentence in sentences:
            clean_sentence, sentence_abbr = self.abbreviations(sentence)
            sentence_token = self.cleaner.get_letter_words(clean_sentence)
            sentence_token = self.cleaner.delete_stop_words(sentence_token)
            tokens = self.tokenizer.get_tokens(' '.join(sentence_token))
            sentences_tokens.append(tokens + sentence_abbr)

        return sentences_tokens

