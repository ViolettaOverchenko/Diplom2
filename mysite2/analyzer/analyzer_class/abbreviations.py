import re


class Abbreviations(object):
    def __init__(self):
        self.re_str_abbr = r"\b[0-9]*[-]*[A-ZА-Я]{1,}[a-zа-я]*[A-ZА-Я]{1,}[-]*[a-zA-Zа-яА-Я0-9]*\b"

    def __call__(self, text):
        abbr = re.findall(self.re_str_abbr, text)
        for word in abbr:
            text = text.replace(word, '')
        return text, abbr

