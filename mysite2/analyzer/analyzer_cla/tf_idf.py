# import math
# from collections import Counter
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# class IDF(object):
#     def __call__(self, word, text):
#         return math.log10(len(text) / sum([1.0 for i in text if word in i]))
#
#
# class TF(object):
#     def __call__(self, text):
#         tf_text = Counter(text)
#         for i in tf_text:
#             tf_text[i] = tf_text[i] / float(len(text))
#         return tf_text
#
#
# class TFIDF(object):
#     def __init__(self):
#         self.tf = TF()
#         self.idf = IDF()
#
#     def __call__(self, text):
#         tf_idf_dictionary_list = []
#         for sentence in text:
#             tf_idf_dictionary = {}
#             tf_dictionary = self.tf(sentence)
#             for word in tf_dictionary:
#                 tf_idf_dictionary[word] = tf_dictionary[word] * self.idf(word, text)
#             tf_idf_dictionary_list.append(tf_idf_dictionary)
#         tf_idf_dictionary = sum_tf_idf(tf_idf_dictionary_list)
#         keys, values = sort(tf_idf_dictionary)
#         return keys, values
#
#
# def sort(dictionary):
#     keys = []
#     values = []
#     sort_dictionary = [(k, dictionary[k]) for k in sorted(dictionary, key=dictionary.get, reverse=True)]
#     for key, value in sort_dictionary:
#         values.append(round(value, 4))
#         keys.append(key)
#     return keys, values
#
#
# def sum_tf_idf(tf_idf_dictionary_list):
#     result_dictionary = {}  # результирующий словарь
#     for dictionary in tf_idf_dictionary_list:  # пробегаем по списку словарей
#         for key in dictionary:  # пробегаем по ключам словаря
#             try:
#                 result_dictionary[key] += dictionary[key]  # складываем значения
#             except KeyError:  # если ключа еще нет - создаем
#                 result_dictionary[key] = dictionary[key]
#
#     return result_dictionary
#
# def graphik(keys, values):
#     lag = 1
#     x = np.arange(0, len(keys), lag)
#     y = values
#     fig = plt.figure()
#     plt.plot(x, y)
#     plt.show()
