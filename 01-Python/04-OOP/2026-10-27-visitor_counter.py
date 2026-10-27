# ==============================================================
# ■ 문제 요약
# Java의 `static` 변수와 `static` 메서드 패턴을 파이썬의 클래스 속성(Class Attribute)과 클래스 메서드(`@classmethod`)로 마이그레이션하는 문제입니다
# 객체가 생성될 때마다 공용 방문자 수(total)가 증가하며, 각 인스턴스는 고유의 방문 순서(number)와 이름(name)을 가져야 합니다
# 인스턴스 내부에 `total`이라는 이름의 속성이 직접 생성되면 안 되며, 클래스 레벨에서 안전하게 관리되어야 합니다
# ==============================================================
# 클래스 변수와 인스턴스 변수의 차이를 이해한다
# ==============================================================

names = input().split()

class Visitor:
    # 클래스 변수를 선언하여 모든 인스턴스가 공유하는 전체 방문자 수(total)를 관리한다
    total = 0 

    def __init__(self, name):
        # 생성자에서 인스턴스 변수 name을 초기화하고, 클래스 변수 total을 1 증가시킨다
        self.name = name 
        Visitor.total += 1
        self.number = Visitor.total # 증가된 total 값을 인스턴스의 방문 번호로 할당

    @classmethod
    def get_total(cls):
        # 클래스 메서드를 통해 전체 방문자 수(total)를 반환한다
        return cls.total # 클래스메서드로 클래스 변수에 직접 접근

    def greet(self):
        # 각 객체의 이름과 몇 번째 방문자인지 포맷팅된 문자열로 반환한다
        return f"{self.name}님, {self.number}번째 방문자입니다"

# 호출부
visitors = [Visitor(name) for name in names]
for v in visitors:
    print(v.greet())
print(Visitor.get_total())
print(Visitor.total == len(visitors), "total" in visitors[0].__dict__)

# ==============================================================
# ■ @classmethod
# @classmethod(클래스 메서드)는 첫 번째 인자로 클래스 자체(cls)를 받는 메서드이다
#
# 데코레이터 사용: 메서드 위에 @classmethod를 붙여서 선언
# 첫 번째 인자 cls: 인스턴스(self) 대신 클래스 객체(cls)가 전달되므로, 클래스 변수에 접근하거나 수정 가능
# 대체 생성자(Alternative Constructor): 객체를 생성하는 다양한 방식을 제공할 때 주로 사용
# 상속 지원: 자식 클래스에서 호출하면 자식 클래스(cls)가 전달되어 상속 구조에서 유연하게 작동
# ==============================================================