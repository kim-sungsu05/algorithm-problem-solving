# ==============================================================
# ■ 문제 요약
# 문장과 금지어를 입력받아 문장에서 금지어를 `***`로 대체하여 출력하는 문제입니다
# 금지어가 문장에 여러 번 등장하면 모두 대체하며 대소문자를 구분합니다
# `replace` 메서드를 사용하지 않고 `for`문과 직접 구현하는 방식입니다
# ==============================================================
# ■ Algorithm
# 1. 원본 문장을 순회한다
# 2. 원본문장의 단어를 다시 순회하여 금지어에 포함될 경우 cnt + 1
# 3. cnt 값이 금지어의 길이와 같아질 경우 '***'로 대체
# 4. 금지어에 포함되지 않는 문자는 전처리없이 내보낸다
# ==============================================================

sentence = input().split()
banned = input()

output = []
banned_len = len(banned)
cnt = 0

for word in sentence:
    side_output = ""

    is_banned = False
    explore_start = False

    for char in word:

        if char in banned:
            cnt += 1
            explore_start = True

            if banned_len == cnt:
                cnt = 0
                side_output += '***'
                is_banned = True

        else:
            side_output += char

    if explore_start and not is_banned:
        output.append(word)
    else:
        output.append(side_output)
    output.append(" ")

print(''.join(output))

# ==============================================================
# ■ 개선점
# 슬라이싱을 통한 정확한 금지어 감지: 문자 단위 검사(`char in banned`) 대신 인덱스 기반 슬라이싱(`word[i:i+banned_len] == banned`)을 사용하여 금지어가 순서대로 정확히 연속될 때만 대체되도록 보장
# 복잡한 플래그 및 카운터 제거: 기존의 여러 플래그 변수(`is_banned`, `explore_start`, `cnt`)를 없애고, `while` 루프를 통한 인덱스 탐색 방식으로 로직을 대폭 단순화
# 출력 방식 개선: 단어마다 공백을 직접 추가하는 방식 대신 `' '.join(output)`을 사용하여 마지막 줄의 불필요한 공백을 방지
# 변수명 가독성 향상: 모호한 의미의 `side_output` 대신 결과 문자열을 뜻하는 `processed_word`로 이름을 변경
# ==============================================================
# ■ 개선 코드

sentence = input().split()
banned = input()

output = []
banned_len = len(banned)

for word in sentence:
    processed_word = ""
    i = 0
    while i < len(word):
        # 슬라이싱으로 연속된 부분 문자열이 금지어와 정확히 일치하는지 확인
        if word[i:i + banned_len] == banned:
            processed_word += '***'
            i += banned_len # 금지어 길이만큼 인덱스 건너뜀
        else:
            processed_word += word[i]
            i += 1
    output.append(processed_word)

# '.join으로 결합해 불필요한 끝 공백 방지
print(' '.join(output))
# ==============================================================