# TextAnalyzer 클래스 정의
class TextAnalyzer:
    def __init__(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            self.text = f.read()

    def word_count(self): # 총 단어 수
        return len(self.text.split())

    def most_common_word(self): # 가장 많이 나온 단어
        from collections import Counter
        words = self.text.split()
        return Counter(words).most_common(1)[0]
    
## 1. class 수정하기 - 함수 추가하기
# TextAnalyzer 클래스 상속받아서 단어 숫자세는 함수 추가하기
class NewTextAnalyzer(TextAnalyzer):
    def target_word_count(self,target_word):
        return self.text.split().count(target_word)