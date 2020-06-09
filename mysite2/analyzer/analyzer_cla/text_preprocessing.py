# from analyzer.analyzer_cla.cleaner import Cleaner
# from analyzer.analyzer_cla.tokenizer import Tokenizer
# from analyzer.analyzer_cla.normalizer import Normalizer
# from analyzer.analyzer_cla.abbreviations import Abbreviations
#
#
# class TextPreprocessing(object):
#     def __init__(self):
#         self.cleaner = Cleaner()
#         self.tokenizer = Tokenizer()
#         self.normalizer = Normalizer()
#         self.abbreviations = Abbreviations()
#
#     def __call__(self, text):
#         sentences = self.tokenizer.get_sentance(text)
#         sentences_tokens = []
#         for sentence in sentences:
#             clean_sentence, sentence_abbr = self.abbreviations(sentence)
#             sentence_token = self.cleaner.get_letter_words(clean_sentence)
#             sentence_token = self.cleaner.delete_stop_words(sentence_token)
#             #sentence_token = self.normalizer.lemma_pymorphy2(sentence_token)
#             #sentence_token = self.cleaner.delete_stop_words(sentence_token)
#             tokens = self.tokenizer.get_tokens(' '.join(sentence_token))
#             sentences_tokens.append(tokens + sentence_abbr)
#
#         return sentences_tokens
#
