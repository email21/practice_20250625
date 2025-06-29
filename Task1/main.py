from module1 import AdvancedTextAnalyzer
def main():
    # 테스트용 파일 생성
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write("hello world hello python world hello")

    # 분석기 객체 생성 및 결과 출력
    analyzer = AdvancedTextAnalyzer('test.txt')
    print("총 단어 수:", analyzer.word_count())
    
    word, count = analyzer.most_common_word()  # 가장 많이 나온 단어와 개수
    print(f"가장 많이 나온 단어는 '{word}'이고, 개수는 {count}번입니다.")
      
    # 미션1 특정 단어 카운팅하기
    with open('test.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    
    print("<위의 문장에서 갯수를 알고 싶은 단어를 입력하세요.>")
    new_word = input()
    print(f"{new_word} 단어 수:", analyzer. target_word_count(new_word))
    
    # 미션2 가장 긴 단어 찾기
    print("가장 긴 단어:", analyzer.longest_word())

if __name__ == "__main__":
    main()
