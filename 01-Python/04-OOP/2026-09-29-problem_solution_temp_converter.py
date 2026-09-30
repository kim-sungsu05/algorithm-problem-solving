# ==============================================================
# ■ 문제 요약
# 객체의 상태(인스턴스 변수)를 사용하지 않는 순수 계산 함수를 클래스 내부에 묶기 위해 @staticmethod 데코레이터를 사용하는 문제입니다. 
# 섭씨를 화씨로 변환하는 c_to_f와 화씨를 섭씨로 변환하는 f_to_c 정적 메서드를 가진 TempConverter 클래스를 정의하여, 
# 클래스명 및 인스턴스 모두를 통해 메서드를 정상적으로 호출할 수 있도록 구현해야 합니다.
# ==============================================================
# ■ Algorithm
# 섭씨 <-> 화씨 온도 변환을 해주는 클래스 작성 후, 내부 메소드는 @staticmethod를 사용하여 객체를 생성하지 않고 결과값만을 출력 
# ==============================================================

class TempConverter:
    """온도 변환을 수행하는 정적 메서드를 포함하는 클래스"""
    
    @staticmethod
    def c_to_f(c: float) -> float:
        """섭씨(Celsius)를 화씨(Fahrenheit)로 변환"""
        return (c * 9 / 5) + 32
        
    @staticmethod
    def f_to_c(f: float) -> float:
        """화씨(Fahrenheit)를 섭씨(Celsius)로 변환"""
        return (f - 32) * 5 / 9

# --- 호출부 (문제 명세에 따라 수정하지 않음) ---
n = int(input())
requests = []
for _ in range(n):
    kind, value = input().split()
    requests.append((kind, float(value)))
    
conv = TempConverter()

for kind, value in requests:
    if kind == "C":
        print(f"{TempConverter.c_to_f(value):.1f}")    # 클래스 이름으로 직접 호출
    else:
        print(f"{conv.f_to_c(value):.1f}")            # 인스턴스로 호출

# ==============================================================
# ■ 데코레이터는 뭘까
# 함수의 특정 행동을 추가해주는(꾸며주는) 역할을 한다 상속과 비슷하지만 상속은 클래스 단위로 이루어지고
# 데코레이터는 메소드 단위로 이루어진다는 점에서 차이가 있다
# @staticmethod(정적 메소드)는 파이썬에 이미 내장되어 있는 데코레이터로, 객체를 생성하지않고 독립적으로 실행되는 유틸리티성 메소드이다

# 장식할 기능 정의 (데코레이터)
def datetime_decorator(func):
    def wrapper():
        print("--- 작업 시작 ---")  # 전처리
        func()                     # 원래 함수 실행
        print("--- 작업 완료 ---")  # 후처리
    return wrapper

# @ 문법으로 적용
@datetime_decorator
def main_work():
    print("핵심 업무 진행 중...")

main_work()
# ==============================================================