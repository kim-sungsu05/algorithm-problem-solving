# ==============================================================
# ■ 문제 요약
# 정수 n과 리스트 items를 한 함수 change_both(num, lst)에 전달했을 때,
# 불변(Immutable) 객체인 int와 가변(Mutable) 객체인 list의 동작 차이를 확인하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 같은 함수 안에서 정숫값을 가지는 변수와 리스트를 수정하고 원본이 바귀는지 확인한다
# ==============================================================

parts = input().split()
n = int(parts[0])
items = [int(x) for x in parts[1:]]

def change_both(num, lst):
    """
    전역변수 n과 items를 함수 내에서 수정하고 원본 전역변수도 수정됐는지 확인하는 함수
    Args:
        num(int): 전역변수 n
        lst(list): 전역변수 items
    Returns:
        None
    """
    num = num + 100
    lst.append(0)

change_both(n, items)
print(n)
print(items)

# ==============================================================