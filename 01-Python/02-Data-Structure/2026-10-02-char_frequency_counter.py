# ==============================================================
# ■ 문제 요약
# 공백을 제외한 입력 문자열 내 각 문자의 등장 횟수를 세고, 문자 사전순(알파벳순)으로 문자: 횟수 형식에 맞춰 한 줄씩 출력하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 1. 문자열을 공백을 제거하여 입력받는다
# 2. 각 문자의 등장 횟수를 세어 오름차순 정렬 후, 문자: 횟수 형식으로 한 줄씩 출력한다
# ==============================================================

def dict_sorted(items):
    """ 딕셔너리를 키의 알파벳 순으로 정렬하는 작업에 사용되는 함수
    Args:
        items(tuple): 빈도수 카운팅 딕셔너리의 단일 items() 값
    Returns:
        str: 알파벳 반환
    """
    return items[0]

string = input().replace(" ", "")
char_count = {}

for char in string:
    # 문자열의 각 문자 빈도수 카운팅
    char_count[char] = char_count.get(char, 0) + 1

# 딕셔너리를 알파벳 (key) 기준으로 오름차순 정렬
sorted_char_count = dict(sorted(char_count.items(), key=dict_sorted))

# 딕셔너리를 순회하여 한 줄 출력
for char, count in sorted_char_count.items():
    print(f"{char}: {count}")

# ==============================================================
# ■ 개선점
# 불필요한 정렬 키 함수(dict_sorted) 제거: 파이썬의 sorted(char_count.items())는 기본적으로 튜플의 첫 번째 원소(Key인 알파벳)를 기준으로 오름차순 정렬한다.
# 따라서 커스텀 정렬 함수(dict_sorted)를 별도로 정의하지 않아도 깔끔하게 정렬할 수 있다.
# Counter 객체 활용: 파이썬 표준 라이브러리 collections.Counter를 사용하면 별도의 반복문과 .get() 호출 없이 한 줄로 요소별 빈도를 집계할 수 있어 파이썬다운(Pythonic) 코드가 된다.
# ==============================================================
# ■ 개선 코드

from collections import Counter

# 공백을 제거한 문자열 입력받기
string = input().replace(" ", "")

# collections.Counter를 활용한 문자 빈도수 자동 카운팅
char_count = Counter(string)

# sorted()는 튜플 (key, value)의 첫 번째 요소인 key(알파벳)를 기준으로 기본 정렬함
for char, count in sorted(char_count.items()):
    print(f"{char}: {count}")
    
# ==============================================================