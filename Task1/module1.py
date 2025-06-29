# TextAnalyzer 클래스 정의
class TextAnalyzer:
    def __init__(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            self.text = f.read()

    def word_count(self): # 글자수?
        return len(self.text.split())

    def most_common_word(self): # 가장 많이 나온 단어
        from collections import Counter
        words = self.text.split()
        return Counter(words).most_common(1)[0]