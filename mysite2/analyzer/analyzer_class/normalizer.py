import maru
import pymorphy2
from datetime import datetime
import time

class Normalizer(object):
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
        self.analyzer = maru.get_analyzer(tagger='crf', lemmatizer='pymorphy')

    def pymorphy2(self, words):
        normal_words = []
        print("pymorphy2")
        start_time = datetime.now()
        for word in words:
            p = self.morph.parse(word)[0]
            normal_words.append(p.normal_form)
            print(p.tag)
        time.sleep(5)
        print(datetime.now() - start_time)
        return normal_words

    def maru(self, words):
        print("maru")
        start_time = datetime.now()
        analyzed = self.analyzer.analyze(words)
        normal_words = []
        for word in analyzed:
            normal_words.append(word.lemma)
        time.sleep(5)
        print(datetime.now() - start_time)
        return normal_words
