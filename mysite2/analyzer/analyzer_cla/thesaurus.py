# from analyzer.analyzer_cla.text_preprocessing import TextPreprocessing
# from analyzer.analyzer_cla.tf_idf import TFIDF
#
#
# class Thesaurus(object):
#     def __init__(self):
#         self.text_preprocessing = TextPreprocessing()
#         self.tf_idf = TFIDF()
#         self.alpha = 0.1
#         self.betta = 0.6
#
#     def __call__(self, text):
#         sentences_tokens = self.text_preprocessing(text)
#         keys, values = self.tf_idf(sentences_tokens)
#
#         return keys, zip(keys, values)
