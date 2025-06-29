# 도서 클래스
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"제목: {self.title}, 저자: {self.author}"
    
# 도서관 클래스
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print("✅ 책이 추가되었습니다.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("🗑️ 책이 삭제되었습니다.")
                return   # 뒤에 아무것도 없으면 종료하라는 의미
        print("❌ 해당 책을 찾을 수 없습니다.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print("🔍 책을 찾았습니다:")
                print(book)
                return
        print("❌ 해당 책이 없습니다.")

    def list_books(self):
        if not self.books:
            print("📚 등록된 책이 없습니다.")
        else:
            print("📚 도서 목록:")
            for book in self.books:
                print(book)