from storage import FileLibrary
import os

# 메인 실행 부분
def main():
    lib = FileLibrary()
    lib.load_all()
    current_user = None
    
    while not current_user:  # 가입된 유저가 없으면 반복
        print("\n1. 로그인  2. 회원가입  3. 종료")
        cmd = input("선택: ")
        if cmd == '1':
            uid = input("아이디: ")
            pw = input("비밀번호: ")
            if lib.login(uid, pw):
                current_user = uid
                print("✅ 로그인 성공")
            else:
                print("❌ 실패")
        elif cmd == '2':
            uid = input("아이디 생성: ")
            pw = input("비번 생성: ")
            if lib.register_user(uid, pw):
                print("✅ 회원가입 완료")
            else:
                print("❌ 이미 존재하는 아이디입니다.")
        else:
            return
    
    while True:
        print("\n1. 책 추가 2. 삭제 3. 검색 4. 목록\n5. 대출 6. 반납 7. 내 책 8. 저장 후 종료")
        sel = input("선택: ")
        if sel == '1':
            lib.add_book(input("제목: "), input("저자: "))
        elif sel == '2':
            lib.remove_book(input("제목: "))
        elif sel == '3':
            lib.search_book(input("제목: "))
        elif sel == '4':
            lib.list_books()
        elif sel == '5':
            lib.borrow_book(current_user, input("제목: "))
        elif sel == '6':
            lib.return_book(current_user, input("제목: "))
        elif sel == '7':
            print(f"\n📦 {current_user}의 대출 목록:")
            for b in lib.loans.get(current_user, []):
                print(b)
        elif sel == '8':
            lib.save_all()
            print("💾 저장 완료. 종료합니다.")
            break

if __name__ == "__main__":
    main()