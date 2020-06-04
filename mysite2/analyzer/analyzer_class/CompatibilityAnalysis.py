

class CompatibilityAnalysis(object):
    def analyze(self, one_keys, two_keys):
        common_keywords = []
        for word in two_keys:
            if word in one_keys:
                common_keywords.append(word)
        results = round(len(common_keywords)/len(two_keys)*100)
        return results