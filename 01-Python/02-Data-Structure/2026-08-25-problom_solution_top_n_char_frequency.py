# ==============================================================
# ■ 문제 요약
# 문자열과 정수 N을 입력받아, 문자열 내 모든 글자의 빈도수를 세고 빈도수가 높은 순(내림차순)으로
# 상위 N개까지 글자: 횟수 형식으로 출력하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 1. 문자열을 입력받아 순회한다
# 2. 한 단어씩 딕셔너리로 빈도수를 카운팅한다
# 3. 순회 종료 후 내림차순으로 정렬한 뒤, 상위 n개를 출력한다
# ==============================================================

word = input()
n = int(input())


# 카운팅용 딕셔너리
word_count = {}

# 문자열 순회
for char in word:

    # 딕셔너리로 빈도 카운팅
    word_count[char] = word_count.get(char, 0) - 1

# 내림차순으로 정렬
top_n_chars = sorted(((count, char) for char, count in word_count.items()))

for idx, (count, char) in enumerate(top_n_chars):

    # 상위 n개만 출력
    if idx == n:
        break

    # -로 저장되어 있기 때문에 한번더 -를 곱해준다
    print(f"{char}: {-count}")

# ==============================================================
# ■ 개선점
# 공백 제외 처리를 추가하면 완전한 코드가 된다. for char in word를
# for char in word.replace(' ', '')이나 if char != ' ' 조건으로 보완.
# 변수명 word는 단어보다 문자열을 의미하므로, text 또는 input_str가 더 명확하다.
# enumerate와 if idx == n: break 대신 top_n_chars[:n]으로 슬라이싱하면 코드가 더 간결해진다.
# ==============================================================
# ■ 리펙토링 코드
text = input()
n = int(input())

char_count = {}

for char in text:
    
    # 공백은 빈도 집계에서 제외
    if char == ' ':
        continue
    # 음수로 저장하여 오름차순 정렬로 내림차순 효과
    char_count[char] = char_count.get(char, 0) - 1

# 빈도 내림차순, 동률 시 알파벳으로 오름차순
top_n_chars = sorted((count, char) for char, count in char_count.items())

# 슬라이싱으로 상위 n개만 출력
for count, char in top_n_chars[:n]:
    # 음수로 저장되어 있으모로 부호를 반전하여 출력
    print(f"{char}: {-count}")
# ==============================================================