# 미션3. 파일 저장/불러오기 : 책 목록, 유저 정보, 대출 정보 저장
import os
from models import LoanLibrary

# data 폴더가 없으면 생성
os.makedirs("data", exist_ok=True)

# 1. 대출 기능 추가한 LonLibrary 상속받아서 기록 관리하는 FileLibrary 만들기
class FileLibrary(LoanLibrary):
    # 2. 현재 존재하는 책, 유저, 대출 정보 txt file 로 저장하기
    # with, open 어쩌구는 일단 "그림"이라 생각하고 읽어주세요. 금욜에 배웁니다.
    def save_all(self):
        # books.txt 라는 곳에 현재 도서관에 존재하는 books 데이터 저장
        with open("data/books.txt", "w", encoding="utf-8") as f:
            for b in self.books:
                f.write(f"{b.title}|{b.author}\n")
        # users.txt 라는 곳에 현재 도서관에 존재하는 users 데이터 저장
        with open("data/users.txt", "w", encoding="utf-8") as f:
            for u in self.users:
                f.write(f"{u.username}|{u.password}\n")
        # loans.txt 라는 곳에 현재 도서관에 존재하는 loans 데이터 저장
        with open("data/loans.txt", "w", encoding="utf-8") as f:
            for u, blist in self.loans.items():
                titles = ",".join([b.title for b in blist])
                f.write(f"{u}:{titles}\n")

    # 3. 저장했던 txt file 들로 부터 데이터 불러오기.
    def load_all(self):
        # 해당 txt file 이 존재하는 지 체크
        if os.path.exists("data/books.txt"):
            with open("data/books.txt", "r", encoding="utf-8") as f:
                for line in f:
                    t, a = line.strip().split("|")
                    self.add_book(t, a)

        if os.path.exists("data/users.txt"):
            with open("data/users.txt", "r", encoding="utf-8") as f:
                for line in f:
                    uid, pw = line.strip().split("|")
                    self.register_user(uid, pw)

        if os.path.exists("data/loans.txt"):
            with open("data/loans.txt", "r", encoding="utf-8") as f:
                for line in f:
                    uid, titles = line.strip().split(":")
                    for t in titles.split(","):
                        book = next((b for b in self.books if b.title == t), None)
                        if book:
                            self.books.remove(book)
                            self.loans.setdefault(uid, []).append(book)