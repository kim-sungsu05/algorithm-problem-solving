# ==============================================================
# ■ 문제 요약
# 상품명(필수), 가격(필수), 임의 개수의 옵션(*options), 키워드 전용 인수인 할인액(discount, 기본값 0)을 입력받아 
# 할인된 최종 금액과 옵션 개수를 계산한 뒤 "{상품명} {최종가격}원 옵션{개수}개" 포맷의 함수를 구현하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 1. 입력 처리를 받는다
# 2. 상품명, 가격, 옵션, 할인액을 입력받아 주문 요약을 반환하는 함수 정의
# ==============================================================

raw = input().split()
pos = [x for x in raw if '=' not in x]
product = pos[0]
price = int(pos[1])
options = pos[2:]
discount = 0

for item in raw:
    if '=' in item:
        k, v = item.split('=')
        if k == 'discount':
            discount = int(v)

def order(product, price, *options, discount=0):
    """상품명, 가격, 옵션, 할인액을 받아 주문 요약을 반환하는 함수입니다.

    Args:
        product (str), price (int), options(tuple), discount (int): 상품명, 가격, 옵션, 할인액

    Returns:
        str: 요약 문자열
    """
    return f"{product} {price - discount}원 옵션{len(options)}개"

print(order(product, price, *options, discount=discount))


# ==============================================================
