# ==============================================================
# ■ 문제 요약
# 1차원 배열(위치 0~9)에서 좌(1)/우(2) 명령을 입력받아 탈출구(위치 9)에 도달하는 시뮬레이션 문제입니다.
# ==============================================================
# ■ Algorithm
# 1. 정수 1과 2를 입력받는다. 입력값은 좌우이며, 이동은 항상 1만큼이다
# 2. 입력받은 정수가 1 또는 2가 아니면 범위 초과 메세지 출력 후 계속한다
# 3. 함정1 (위치 3), 함정2 (위치 7)은 한번 진입을 한 경우, 플래그 변수를 사용하여 일반 통로로 변환한다
# 4. 보물(위치 5)도 마찬가지로 첫 방문시만 +10
# 5. 탈출구 (위치 9)를 만나면 종료
# ==============================================================

pos = 0  # 현재 위치
total_moves = 0  # 총 이동횟수
trap1 = 3  # 함정 1 위치
trap2 = 7  # 함정 2 위치
treasure = 5  # 보물 위치
exit_pos = 9  # 탈출구 위치 
got_treasure = 0  # 보물 획득 시 스코어


# 플래그 변수를 사용하여 함정과 보물을 처음 마주쳤을 때 한번만 유효화
is_saw_trap_1 = False
is_saw_trap_2 = False
is_saw_treasure = False


print("=== 1차원 미로 탈출 ===")
print("탈출구는 위치 9입니다. 함정을 피하고 보물을 찾으세요!")
print(f"현재 위치: {pos}")

# 탈출구를 찾을 때까지 무한반복
while True:

    # 입력값을 현재 위치와 총 이동횟수 변수에 누적 합
    move = int(input())

    if move != 1 and move != 2:
        print("1 또는 2를 입력하세요.")
        continue

    pos += 1
    total_moves += 1


    # 현재 위치가 3일 경우, 0으로 이동
    if pos == 3 and not is_saw_trap_1:
        pos = 0
        print(f"함정! 위치 {pos}으로 되돌아갑니다!")
        is_saw_trap_1 = True


    # 현재 위치가 5일 경우 got_treasure += 1
    if pos == 5 and not is_saw_treasure:
        got_treasure += 10
        print(f"보물 발견! 점수 +{got_treasure}!")
        is_saw_treasure = True


    # 현재 위치가 7일 경우 위치 4로 이동
    if pos == 7 and not is_saw_trap_2:
        pos = 4
        print(f"함정! 위치 {pos}로 되돌아갑니다!")
        is_saw_trap_2 = True
 

    # 현재 위치가 9일 경우 반복 종료
    if pos == 9:
        print("탈출구에 도달했습니다!")
        print(f"현재 위치: {pos}")
        break

    print(f"현재 위치: {pos}")

# 총 이동 횟수와 점수 출력
print(f"탈출 성공! 총 이동 횟수: {total_moves}, 점수: {got_treasure}")

# ==============================================================
# ■ 개선점
# 왼쪽(1) 이동에 대한 범위 초과 처리 누락 문제가 있다. 1이 입력 되었을 때 (즉, 왼쪽일 때)
# pos -= 1로 분기해야하는데 현재는 pos += 1로만 하고 있다. 이동 후 위치가 0~9 범위를 벗어나면
# 범위초과 메세지 출력 후, pos 변경하지 않은 채 continue
# got_treasure은 점수를 나타내므로 score로 이름을 바꾸는 것이 좋다.
# ==============================================================

# 해당 조건 필터링을 추가하여 왼쪽 분기도 처리
while True:
    ...

    delta = -1 if move == 1 else 1
    
    new_pos = pos + delta

    if new_pos < 0 or new_pos > exit_pos:
        print("이동할 수 없습니다! (범위 초과)")
        continue

    pos = new_pos
    total_moves += 1
    ...