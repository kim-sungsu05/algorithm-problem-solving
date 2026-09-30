# ==============================================================
# ■ 문제 요약
# 공백으로 구분된 영문 소문자 단어들을 입력받아 각 알파벳 순서에 대응하는 점수(a=1, b=2, ..., z=26)의 합을 계산한 후, 
# 입력 순서대로 단어: 점수 형식으로 한 줄씩 출력하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 1. 문자열 "abcd...xyz" 문자열에서 각 인덱스 자리에 +1을 하여 딕셔너리로 저장한다 (문자열 점수)
# 2. 입력받은 words를 순회하며 루프변수를 딕셔너리의 키로 넣어 값을 누적하여 저장
# 3. 반복이 끝난 뒤, 최종 점수 출력
# ==============================================================

import string

words = input().split()

# 문자열 점수 저장
alphabets = string.ascii_lowercase
alphabet_scores = {char : alphabets.index(char)+1 for char in alphabets}

# 문자열을 순회하며 점수를 저장
for word in words:

    score = 0

    for char in str(word):
        score += alphabet_scores[char]

    print(f"{word}: {score}")

# ==============================================================
# ■ 개선점
# "abcdefghijklmnopqrstuvwxyz".index(c) + 1 를 직접 사용하면 import string과 딕셔너리 선언없이 더 간결하게 표현될 수 있다.
# (이 문제에서는 오타가 날까봐 string 패키지와 딕셔너리 사용, 상황에 맞게 우연하게 쓸 것)
# str(word)는 word가 이미 문자열이므로 불필요한 변환이다.
# 점수 누적에 `sum(alphabet_scores[c] for c in word)` 처럼 내장 sum()과 제너레이터 표현식을 활용하면 내부 루프를 한 줄로 줄일 수 있다.
# 딕셔너리 컴프레이션 대신 `ord(c) - ord('a') + 1`을 이용하면 별도 자료구조 없이 O(1)로 점수를 구할 수 있다.
# ==============================================================
# ■ 리펙토링 코드

import string

words = input().split()

# 문자별 점수 저장
alphabets = string.ascii_lowercase
alphabet_scores = {char: alphabets.index(char) + 1 for char in alphabets}

# 문자열을 순회하여 점수를 저장
for word in words:
    score = sum(alphabet_scores[char] for char in word)  # sum()으로 내부 루프 간소화; str() 변환 불필요
    print(f"{word}: {score}")
# ==============================================================