# ==============================================================
# ■ 문제 요약
# 불용어(stopwords) set이 주어질 때, 입력받은 텍스트를 소문자로 정규화하고 공백 기준으로 분리합니다.
# 불용어에 포함된 단어를 제외하고 남은 단어들의 빈도를 카운팅합니다.
# 빈도가 높은 순서대로(빈도가 같다면 알파벳 오름차순으로) 정렬하여 상위 최대 3개의 단어와 빈도수를 지정된 형식으로 출력하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 1. 입력받은 문자열을 띄어쓰기 기준으로 분리하여 리스트로 변환하고 소문자로 정규화한다
# 2. 문자열 리스트를 순회하여 stopwords에 포함될 경우 건너뛴다
# 3. stopwords에 포함되지 않을 경우 해당 단어를 카운팅한다
# 4. 카운팅이 가장 높은 순서대로 3개의 단어 출력, 3개가 안 될 경우 있는 만큼 출력한다
# ==============================================================

stopwords = {"a", "an", "the", "is", "are", "in", "on", "at", "and", "or", "but"}
text = input().lower().split()

word_counting = {}

for word in text:
    if word not in stopwords:
        word_counting[word] = word_counting.get(word, 0) - 1

top_3_words = tuple(sorted((counting, word) for word, counting in word_counting.items()))

if len(top_3_words) < 3:
    for idx in range(len(top_3_words)):
        print(f"{top_3_words[idx][1]}: {top_3_words[idx][0] * -1}")

else:
    for idx in range(3):
        print(f"{top_3_words[idx][1]}: {top_3_words[idx][0] * -1}")

# ==============================================================
# ■ 개선점
# 정렬 키에서 음수 처리: 빈도를 음수로 미리 저장하는 대신 양수 그대로 두고, `lambda` 정렬 키 내부(`-x[1]`)에서 처리하면 가독성을 높일 수 있다.
# 슬라이싱을 통한 분기 제거: `[:3]` 슬라이싱을 사용하여 단어 개수가 3개 미만인 경우와 이상인 경우를 별도의 `if-else` 없이 하나의 반복문으로 처리할 수 있다.
# 튜플 언패킹 적용: 인덱스 변수(`idx`)를 사용해 접근하던 방식에서 벗어나, `for word, count in ...` 형태의 언패킹을 적용하면 더 파이썬다운 코드가 된다.
# ==============================================================
# ■ 개선 코드

word_counting = {}

for word in text:
    # 불용어가 아닌 단어만 카운팅 (양수 그대로 저장)
    if word not in stopwords:
        word_counting[word] = word_counting.get(word, 0) + 1

# 정렬 키: 빈도 내림차순(-count), 동률은 알파벳 오름차순(word)
top_3_words = sorted(word_counting.items(), key=lambda x: (-x[1], x[0]))

# [:3] 슬라이싱으로 3개 미만/이상 모두 처리
for word, count in top_3_words[:3]:
    print(f"{word}: {count}")

# ==============================================================