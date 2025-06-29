from module import Library

# 메인 실행 부분
def main():
    lib = Library()  # 객체생성 lib

    while True:
        print("\n📘 도서관 관리 프로그램")
        print("1. 책 추가")
        print("2. 책 삭제")
        print("3. 책 검색")
        print("4. 책 목록 보기")
        print("5. 종료")

        choice = input("원하는 작업을 선택하세요 (1-5): ")

        if choice == '1':
            title = input("책 제목: ")
            author = input("책 저자: ")
            lib.add_book(title, author)

        elif choice == '2':
            title = input("삭제할 책 제목: ")
            lib.remove_book(title)

        elif choice == '3':
            title = input("검색할 책 제목: ")
            lib.search_book(title)

        elif choice == '4':
            lib.list_books()

        elif choice == '5':
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("❗ 유효하지 않은 입력입니다. 1~5 중 선택해주세요.")
            
if __name__ == "__main__":
    main()