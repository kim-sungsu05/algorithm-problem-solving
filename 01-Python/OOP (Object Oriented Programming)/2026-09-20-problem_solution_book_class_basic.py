# ==============================================================
# ■ 문제 요약
# 도서의 제목(title), 저자(author), 페이지 수(pages)를 인스턴스 속성으로 저장하는 Book 클래스를 정의하고, 
# 정해진 형식의 문자열을 반환하는 describe() 메서드와 페이지 수가 300장 이상인지 판별하여 불리언 값을 반환하는 is_long() 메서드를 구현하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 클래스 안에 도서 정보를 반환하는 메서드를 작성한 후, 클래스를 호출하여 메서드 반환값 출력
# ==============================================================

class Book:
    # 생성자로 변수 초기화
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # 도서 정보 반환 메서드
    def describe(self):
        # 메서드 내부에서는 항상 self로 인스턴스 속성 접근
        return f"{self.title} - {self.author} ({self.pages}쪽)"
        
    # 페이지에 따라 True 또는 False 반환
    def is_long(self):
        return self.pages >= 300

n = int(input())
rows = [input().split() for _ in range(n)]

# 호출부
for title, author, pages in rows:
    book = Book(title, author, int(pages))
    print(book.describe())
    print(book.is_long())

# ==============================================================
# ■ 개선점
# 매직 메서드(__str__ / __repr__) 활용: describe() 메서드 대신 __str__ 매직 메서드를 구현하면 print(book) 호출만으로도 직관적으로 객체 정보를 확인할 수 있다.
# 클래스 문서화(Docstring): 클래스 선언 바로 아래에 """도서 정보를 저장하고 관련 기능을 제공하는 클래스"""와 같이 독스트링을 추가하면 협업 시 가독성이 크게 향상
# 방어적 프로그래밍 도입: 생성자 내부에 assert pages >= 0 조건이나 예외 처리 로직을 추가하여, 음수 페이지 수와 같은 비정상적인 데이터 입력을 미연에 방지하는 것이 좋다.
# ==============================================================
# ■ 개선 코드

class Book:
    """도서 정보를 저장하고 관련 기능을 제공하는 클래스"""

    # 생성자로 변수 초기화
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # 도서 정보 반환 메서드
    def describe(self):
        # 메서드 내부에서는 항상 self로 인스턴스 속성 접근
        return f"{self.title} - {self.author} ({self.pages}쪽)"

    # 페이지에 따라 True 또는 False 반환
    def is_long(self):
        return self.pages >= 300

    def __repr__(self):  # 디버깅 시 book 객체를 바로 확인할 수 있도록 추가
        return f"Book({self.title!r}, {self.author!r}, {self.pages})"


n = int(input())
rows = [input().split() for _ in range(n)]

# 호출부
for title, author, pages in rows:
    book = Book(title, author, int(pages))
    print(book.describe())
    print(book.is_long())

# ==============================================================
# ■ __str__ / __repr__ 는 뭘까
# 
# __str__과 __repr__은 객체를 문자열로 표현할 때 사용 목적에 따라 나누어 쓰는 파이썬의 특수 메서드
# __str__은 일반 사용자(User)용, __repr__은 개발자(Developer)용
# 
# __str__ : 읽기 편한 형태 | print(), str()로 호출 | 무슨 데이터인지 쉽게 알아보기 위하여
# __repr__ : 명확하고 정확한 정보(디버깅) | 파이썬 대화형 터미널(REPL), repr(), 리스트 출력 시 호출 | 어떻게 만들어진 객체인지 코드로 복원 가능하게


# -------- 예시 코드 --------


# 표준 라이브러리 예시
import datetime

today = datetime.date.today()

# __str__ : 사용자가 보기 편한 포맷
print(str(today))   # 2026-09-20

# __repr__ : 어떤 클래스와 인자로 만들어졌는지 명확한 표현
print(repr(today))  # datetime.date(2026, 9, 20)

# -------------------------------------------------------

# 클래스에서 직접 구현
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 사용자용: 보기 깔끔하게 출력
    def __str__(self):
        return f"{self.name}({self.age}세)"

    # 개발자용: 객체의 생김새를 정확히 묘사
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("홍길동", 20)

print(p)         # __str__ 호출  -> 홍길동(20세)
print(str(p))    # __str__ 호출  -> 홍길동(20세)

print(repr(p))   # __repr__ 호출 -> Person(name='홍길동', age=20)
print([p])       # 리스트 안에 넣고 출력할 땐 __repr__ 호출 -> [Person(name='홍길동', age=20)]

# ==============================================================
# ■ 인스턴스와 self는 뭘까
# 
# 인스턴스 (instance): class를 바탕으로 메모리에 실체화된 결과물
# 
# self: 클래스 내부 메서드에서 `지금 이 코드를 실행하고 있는 바로 그 인스턴스` 를 집어내기 위해 쓰는 첫번째 매개변수, 자바의 `this`와 같은 개념
# 자바는 `this`가 컴파일러에 의해 암묵적으로 제공되지만, 파이썬은 메서드를 정의할 때 첫 번째 매개변수로 `self`를 직접 적어줘야 한다는 명시적인 차이가 있다
# 
# 변수를 나중에도 계속 기억해야하는지, 아니면 계산할 때 잠깐 쓰고 버릴 것인지에 따라 self. 을 붙일지 말지 결정한다
# - self.변수 (인스턴스 변수): 객체가 살아있는 동안 영구적으로 저장, 다른 메서드에서 쓸 때, 밖에서 꺼내 쓸 때
# - 그냥 변수 (지역변수):      메서드가 실행되는 동안만 잠깐 존재, 메서드가 종료되면 메모리에서 사라짐
# 
# 파이썬은 Explicit is better than implicit (명시적인 것이 암시적인 것보다 낫다)는 디자인 철학을 가지고 있어 이렇게 한다
# 근데 왜 변수 자료형 지정을 안해도 동적으로 처리해 주나 --> 파이썬 에서 명시적이라는 것은 문법을 길게 적으라는 것이 아닌 코드가 눈속임없이 직관적으로 보이게 만들라는 의미
# x = 10은 너무 명확, 반면 self.x 라고 적는 건 이게 지역변수인지 인스턴스 변수인지 눈으로 바로 구분하게 하기 위해서 필요하다
# 만약 변수 타입도 명시하고 싶으면 아래처럼 명시할 수도 있다
name: str = "홍길동"
age: int = 20


# -------- 예시 코드 --------

# self와 인스턴스
class Dog:
    def __init__(self, name):
        # self.name: 이 인스턴스만의 name 변수에 전달받은 값을 저장
        self.name = name

    def bark(self):
        # self.name: 호출한 인스턴스의 name을 가져옴
        print(f"{self.name}가 멍멍")

# dog1과 dog2는 서로 다른 '인스턴스'
dog1 = Dog("바둑이")
dog2 = Dog("초코")

# dog1.bark()를 실행할 때 파이썬 내부적으로는 Dog.bark(dog1)처럼 self에 dog1을 전달
dog1.bark()  # 바둑이가 멍멍
dog2.bark()  # 초코가 멍멍



# 인스턴스 변수와 지역변수
class Character:
    def __init__(self, name, hp):
        # 인스턴스 변수: 캐릭터가 계속 유지해야 하는 정보
        self.name = name
        self.hp = hp

    def take_damage(self, raw_damage):
        # 지역 변수: 데미지 계산할 때만 잠깐 쓰고 버릴 임시 값
        defense = 10
        actual_damage = raw_damage - defense
        
        # 임시로 계산한 값(actual_damage)을 영구 데이터(self.hp)에 반영
        self.hp -= actual_damage
        print(f"{self.name}가 {actual_damage}의 데미지를 입었습니다!")

        # 객테 생성 후, 메서드 호출 (괄호 안의 30이 raw_damage 전달)
        # player.raw_damage(30)

    def check_status(self):
        # self.hp는 인스턴스 변수라 다른 메서드에서 바뀐 값도 그대로 기억함
        print(f"{self.name}의 현재 체력: {self.hp}")
        
        # print(defense)  <- 에러 발생, defense는 take_damage 안에서 이미 사라진 지역 변수
# ==============================================================