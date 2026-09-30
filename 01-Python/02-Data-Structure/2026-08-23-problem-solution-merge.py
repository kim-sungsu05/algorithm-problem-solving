# ==============================================================
# ■ 문제 요약
# 두 줄로 각각 정렬되어 입력되는 정수 리스트 두 개를 하나로 병합(Merge)하여,
# 전체가 오름차순으로 정렬된 결과를 공백 구분 문자열로 출력하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 1. a, b리스트를 묶어서 같이 순회한다
# 2. 두 리스트의 요소를 차례로 merge 리스트에 넣으면서 원본 리스트에서는 제거한다
# 3. 순회가 끝났지만 리스트 길이가 서로 달라, 들어가지 못한 요소가 있다면 한 번에 merge에 추가한다
# 4. 오름차순 정렬한 뒤 출력한다
# ==============================================================

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

# 두 리스트를 병합한 결과를 담을 리스트
merge_list = []

for values in zip(a, b):

    # a와 b의 요소를 한번에 삽입
    merge_list.extend(values)

    # merge_list에 추가한 a와 b의 요소 삭제
    a.remove(values[0])
    b.remove(values[1])


# a 혹은 b 리스트에 요소가 남아 있을 경우 전부 추가
if a:
    merge_list.extend(a)
if b:
    merge_list.extend(b)

merge_list.sort()
print(' '.join(map(str, merge_list)))

# ==============================================================
# ■ 개선점
# merge 알고리즘 (두 포인터)를 사용하지 않았다. zip으로 묶고 마지막에 sort호출은
# 단순 합산 후 정렬이다. 또한 remove()는 리스트 전체 순회이기 때문에 비효율적이다.
# merge 알고리즘은 두 포인터 i, j를 두고 a[i]와 b[j]를 두고 비교하며 작은 쪽을 결과에 추가하고
# 해당 포인터만 전진하는 방식으로 O(n) 시간 복잡도로 동작한다.
# ==============================================================
# ■ 리펙토링 코드
merged = []

idx_a = 0
idx_b = 0

# 두 포인터가 각각 리스트 끝에 도달할 때까지 비교, 삽입
while idx_a < len(a) and idx_b < len(b):
    if a[idx_a] < b[idx_b]:
        merged.append(a[idx_a])
        idx_a += 1
    else:
        merged.append(b[idx_b])
        idx_b += 1

# a 혹은 b 리스트에 요소가 남아 있을 경우 전부 추가
if idx_a < len(a):
    merged.extend(a[idx_a:])    

if idx_b < len(b):
    merged.extend(b[idx_b:])

print(' '.join(map(str, merged)))
# ==============================================================