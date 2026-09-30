# ==============================================================
# ■ 문제 요약
# 양의 정수 (N >= 6)을 입력받아 2 이상 N 이하에 존재하는 모든 소수를 구하고, 
# 연속된 소수 쌍 간의 차이(간격) 중 가장 큰 간격을 가지는 소수 쌍과 그 간격을 출력하는 문제입니다. 
# (단, 최대 간격을 가진 소수 쌍이 여러 개 존재할 경우 가장 먼저 발견된 소수 쌍을 출력합니다.)
# ==============================================================
# ■ Algorithm
# 1. 2부터 n까지 순회하며 소수들을 찾는다
# 2. 기본값으로 prev = None으로 초기화
# 3. 현재 소수값을 리스트와 cur 변수에 저장 후, prev가 None이 아닌 경우만 prev값과의 차를 minus_value변수에 저장한다 (prev는 분기 마지막에 cur로 갱신)
# 4. minus_value값이 max_diff보다 크 경우 max_diff를 새로 갱신한다
# 5. 순회가 끝난 뒤, 소수 목록과 max값을 출력한다
# ==============================================================

n = int(input())
while n < 6:
    n = int(input())

prime_nums = []
max_diff = 0
prev = None

# 2, n만큼 순회
for cur in range(2, n + 1):

    # 소수인 지 판별
    for num in range(2, int(cur**0.5) + 1):
        if cur % num == 0:
            break  # 소수가 아닌 경우 건너뜀
    else:
        prime_nums.append(cur)  # prime_nums 리스트에 추가

        # prev값이 None이 아닌 경우, 즉 이전값이 존재하는 경우 실행
        if prev is not None:
            minus_value = cur - prev

            if minus_value > max_diff:
                max_diff = minus_value
                left_value, right_value = prev, cur

        prev = cur  # 현재 소수값을 다음 분기의 이전 값으로 사용하기 위해 prev에 대입

# 소수 목록과 max값 출력
print(f"소수 목록: {' '.join(map(str, prime_nums))}")
print(f"최대 간격: {left_value}와 {right_value} 사이 (간격: {max_diff})")

# ==============================================================
# ■ 개선점
# n이 매우 클 경우를 대비해 에라토스테네스의 체를 활용하면 사간 복잡도를 O(N log log N)로 줄일 수 있다.
# `prev`변수 없이 `prime_nums`리스트로 채운 뒤 `zip(prime_nums, prime_nums[1:])`로 인접쌍을
# 순회하면 코드 구조를 더 간결하게 표현할 수 있습니다.
# ==============================================================
# ■ `zip(prime_nums, prime_nums[1:])` 로 개선한 구조

# 2부터 n까지 순회하며 소수 판별
for cur in range(2, n + 1):
    for num in range(2, int(cur ** 0.5) + 1):
        if cur % num == 0:
            break  # 소수가 아닐 경우 건너뜀
    else:
        prime_nums.append(cur)  # prime_nums 리스트에 추가

# 인접 소수 쌍을 zip으로 순회하여 최대 간격 탐색
# zip(prime_nums, prime_nums[1:]) 을 사용하면 prev 변수 없이 깔끔하게 처리 가능
for prev_prime, next_prime in zip(prime_nums, prime_nums[1:]):
    gap = next_prime - prev_prime
    if gap > max_diff:  # 더 큰 간격 발견 시 갱신 (같은 값이면 첫 번째 쌍 유지)
        max_diff = gap
        left_value, right_value = prev_prime, next_prime

# ==============================================================
# ■ 에라토스테네스의 체
# 소수가 아닌 합성수들을 체로 걸러내서 소수만 남기는 알고리즘이다.
# ex) 2부터 N까지의 숫자를 나열한 뒤, 가장 작은 소수는 2이므로 2의 배수(합성수)들을 모두 제거한다
# 이 다음 작은 소수는 3이므로 3의 배수를 모두 제거한다. 이런 식으로 √N 이하의 수까지 똑같이 지워나가면
# 최종적으로는 소수만 남게 된다. 선형시간 (O(N)에 가까울 정도로 빠르게 N까지의 모든 소수를 구해낸다

# 코드 예
n = 100 

# 1. 전부 소수(True)로 일단 설정 (0, 1은 제외)
sieve = [True] * (n + 1)

# 2. 배수들 다 지우기 (루트 n까지만)
for i in range(2, int(n**0.5) + 1):
    if sieve[i]:
        # 시작값 (i * i): i = 5일 때, 5 * 2 = 10, 5 * 3 = 15, 5 * 4 = 20은 이미 2와 3의 배수를 지울 때 다 지워졌다.
        # 따라서 아직 지워지지 않은 최솟값인 i * i (5 * 5 = 25)부터 지운다
        
        # 증가폭 (i): i만큼 건너뛰면서 i의 배수만 집어낸다. (i = 3이면 9, 12, 15, 18...)
        for j in range(i * i, n + 1, i):
            sieve[j] = False

# 3. True로 남아있는 인덱스(소수)만 추출
primes = [i for i in range(2, n + 1) if sieve[i]]

print(primes)



# ==============================================================
