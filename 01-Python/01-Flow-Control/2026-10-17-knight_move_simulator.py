# ==============================================================
# ■ 문제 요약
# 8 x 8 체스판에서 나이트의 현재 위치(행, 열)를 입력받아, 
# 나이트가 L자 형태로 이동할 수 있는 모든 위치 중 체스판 범위를 벗어나지 않는 위치들을 찾아 정렬된 순서대로 출력하는 문제입니다.
# (리스트, 딕셔너리, 함수 사용 금지 변수만 사용)
# ==============================================================
# ■ Algorithm
# 1. 나이트가 이동할 수 있는 경우의 수가 범위를 넘어가지 않는 한, 최대 8가지이므로 8번 반복한다
# 2. 조건문을 분기하여 1 or 2, + or - 연산 후, 출력한다
# 3. 연산 과정에서 체스판 범위 (0~7)을 넘어갈 경우는 건너뛴다
# ==============================================================

line = input().split()
row, col = int(line[0]), int(line[1])

prev_col_value = 0    

for i in range(8):
    # 행은 동일한 수가 2번 반복되는 구간이 범위를 넘어가지 않는다는 가정하에, 총 4번 존재한다
    # 그러므로 행을 가장 작은 순으로 출력할 수 있는 -2, -1, +1, +2 연산 순으로 반복하여 행을 구한다

    row_print_value = 0
    col_print_value = 0

    if i == 0 or i == 1:    # 처음과 두 번째 행에 2를 뺀다
        row_print_value = row - 2

    elif i == 2 or i == 3:  
        row_print_value = row - 1

    elif i == 4 or i == 5:  
        row_print_value = row + 1

    elif i == 6 or i == 7:  
        row_print_value = row + 2


    # 행이 2와 연산되었을 경우, 열은 1로만 해야한다는 조건이 있기 때문에 열의 연산을 1만으로 제한
    # 반대로 행이 1과 연산되었을 경우, 열은 2로만 연산되도록 제한

    # 행에 -2 or +2 연산이 된 경우
    if row_print_value + 2 == row or row_print_value - 2 == row:
        col_print_value = col - 1

        # 이미 전 분기에서 -1 연산을 한 경우, +1 연산
        if col_print_value == prev_col_value:
            col_print_value = col + 1

        prev_col_value = col_print_value

    # 행에 -1 or +1 연산이 된 경우
    else:
        col_print_value = col - 2

        # 이미 전 분기에서 -2 연산을 한 경우, +2 연산
        if col_print_value == prev_col_value:
            col_print_value = col + 2

        prev_col_value = col_print_value


    # 연산 결과가 체스 범위를 넘어설 경우 건너뜀
    if row_print_value > 7 or row_print_value < 0  or col_print_value > 7 or col_print_value < 0:
        continue
    else:
        print(row_print_value, col_print_value)

# ==============================================================
# ■ 개선점
# prev_col_value를 이용해 이전 열 값과 비교하는 방식은 논리가 다소 취약하다.
# 예를 들어 col이 0이거나 7인 경우처럼 -1 또는 +1 결과가 경계에 걸릴 때, 
# 우연히 prev_col_value가 같은 값을 가지면 잘못된 분기로 이어질 수 있다. 현재 테스트는 통과했지만, 
# 더 다양한 입력에서도 안전하게 동작하려면 각 반복(i)에서 열 연산을 조건(i가 짝수/홀수)으로 명확히 결정하는 것이 좋다
# ==============================================================