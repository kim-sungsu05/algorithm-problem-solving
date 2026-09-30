# ==============================================================
# ■ 문제 요약
# 두 줄에 걸쳐 입력된 두 단어가 정확히 1회의 편집 작업(길이가 같을 때 1글자 치환, 
# 또는 길이 차이가 1일 때 1글자 삽입/삭제)으로 동일해질 수 있는지 판별하여 
# yes 또는 no를 출력하는 편집 거리(Edit Distance) 검사 문제입니다. 
# (0회 변환으로 이미 동일하거나 2회 이상의 변환이 필요한 경우 no 출력)

# ==============================================================
# ■ Algorithm
# 1. 입력받은 두 단어의 길이가 같은 경우, 두 리스트를 순회하여 다른 글자가 1개 이하일 경우, 'yes' 출력
# 2. 두 단어의 길이가 다를 경우, 긴 단어를 순회하여 요소를 한 개씩 제거해본다
# 3. 요소 한 개를 제거한 값 중 짧은 쪽의 단어가 동일할 경우 'yes' 출력
# 4. 동일하지 않을 경우 'no' 출력

# ==============================================================

word_a = input()
word_b = input()

# 두 단어의 길이가 동일할 경우
if len(word_a) == len(word_b):

    different = 0

    # 두 단어를 동시에 순회
    for a, b in zip(list(word_a), list(word_b)):

        # 두 단어 중 다른 글자가 있을 경우 different += 1
        if a != b:
            different += 1

    # different가 1일 경우 'yes' 출력
    if different == 1:
        print("yes")
    # 0일 경우와 1초과일 경우 'no' 출력
    else:
        print("no")

# 두 단어의 길이가 동일하지 않은 경우
else:
    # 제일 긴 단어를 default_word에 저장
    default_word = list(word_a) if len(word_a) > len(word_b) else list(word_b)
    second_word = list(word_b) if len(default_word) == len(word_a) else list(word_a)

    # default_word의 인덱스를 하나씩 제거하며 길이가 더 짧은 단어와 대조
    # (삽입, 삭제, 치환은 각 1회만 가능하므로 인덱스를 하나씩 제거하며 비교)
    for idx in range(len(default_word)):

        copy_default_word = default_word[:]
        del copy_default_word[idx]

        # 동일할 경우 'yes' 출력 후 종료
        if copy_default_word == second_word:
            print("yes")
            break
    else:
        print("no")
        
# ==============================================================
# ■ 개선점
# default_word는 의미가 명확하지 않다 diff_count 혹은 longer_word가 더 적절하다
# second_word를 결정할 때 min()/max()함수나 간단한 조건식으로 정리하면 깔끔해진다
# 길이 차이가 1보다 큰 경우를 먼저 걸러내는 조건을 추가하면 불필요한 연산을 줄일 수 있다
# 문자열은 이미 이터러블이기 때문에 list() 변환이 불필요하다 zip(list(word_a), list(word_b))대신 zip(word_a, word_b)사용
# 
# ==============================================================
# ■ 리펙토링 코드
word_a = input()
word_b = input()

if len(word_a) == len(word_b):
    # list() 불필요 — 문자열은 이미 이터러블
    diff_count = sum(1 for a, b in zip(word_a, word_b) if a != b)  # 다른 글자 수 계산

    if diff_count == 1:
        print("yes")
    else:
        print("no")

elif abs(len(word_a) - len(word_b)) == 1:  # 길이 차이가 정확히 1인 경우만 처리
    # 더 긴 단어와 더 짧은 단어를 명확히 구분
    longer_word = list(word_a) if len(word_a) > len(word_b) else list(word_b)
    shorter_word = word_b if len(word_a) > len(word_b) else word_a

    # longer_word의 인덱스를 하나씩 제거하며 shorter_word와 대조
    for idx in range(len(longer_word)):
        copy_longer = longer_word[:]
        del copy_longer[idx]

        if copy_longer == list(shorter_word):  # 동일하면 'yes' 출력 후 종료
            print("yes")
            break
    else:
        print("no")

else:  # 길이 차이가 2 이상인 경우 즉시 'no'
    print("no")
    
# ==============================================================