from module1 import TextAnalyzer

def main():
    # 테스트용 파일 생성
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write("hello world hello python world hello")

    # 분석기 객체 생성 및 결과 출력
    analyzer = TextAnalyzer('test.txt')
    print("총 단어 수:", analyzer.word_count())
    print("가장 많이 나온 단어:", analyzer.most_common_word())

if __name__ == "__main__":
    main()
