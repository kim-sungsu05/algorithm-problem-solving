# ==============================================================
# ■ 문제 요약
# 비밀번호 길이 $N$을 입력받아 알파벳 소문자(a~z)와 숫자(1~9, 0)를 교대로 배치한 비밀번호를 생성하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 1. 알파벳과 0부터 9까지의 수가 담긴 리스트를 만든다.
# 2. n만큼 반복하여 알파벳, 숫자 순으로 비밀번호를 생성한다
# 3. z를 넘으면 a부터, 9를 넘으면 0부터 반복
# ==============================================================

n = int(input())

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

alpabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']

password = []

num_count = 0
alpa_count = 0

for idx in range(n):

    if idx % 2 == 0:
        # 끝나면 처음 요소부터 다시 시작
        alpabet = alpabets[alpa_count % len(alpabets)]
        password.append(alpabet)
        alpa_count += 1

    else:
        num = nums[num_count % len(nums)]
        password.append(num)
        num_count += 1

print(''.join(map(str, password)))

# ==============================================================
# ■ 개선점
# 알파벳 리스트에 'v'가 빠져있다. 리스트를 직접 작성하는 대신 string.ascii_lowercase나
# chr() 함수를 활용하면 오타실수를 방지할 수 있다.
# 변수명 alpabets는 오타다 alphabets로 수정하고 오타 없는 명확한 이름으로 작성하기
# ==============================================================
# 개선점을 반영한 리스트 수정

import string

alphabets = list(string.ascii_lowercase)
nums = list(range(1, 10)) + [0]

print(alphabets)