# import pymorphy2
#
#
# class Normalizer(object):
#     def __init__(self):
#         self.morph = pymorphy2.MorphAnalyzer()
#
#     def lemma_pymorphy2(self, words):
#         normal_words = []
#         for word in words:
#             p = self.morph.parse(word)[0]
#             normal_words.append(p.normal_form)
#         return normal_words
