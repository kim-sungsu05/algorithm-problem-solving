# 🧩 Studying Algorithms and Data Structures

### Big-O Notation

```
O(1): 상수시간 | O(log n): 로그시간 | O(n): 선형시간

O(n log n): 선형로그시간 | O(n^2): 이차시간 | O(2^n): 지수시간 
```
O(n^2)과 O(2^n)은 데이터양이 많아질 수록 처리 시간이 급격하게 증가하므로 (지수함수)<br>O(log n) 혹은 O(n), O(1) 수준으로 시간복잡도를 최적화할 필요가 있다
<br><br>O(n^2)은 대표적으로 2중 반복문에서 발생하며 이미 확인한 데이터를 set과 같은 자료구조에 저장하여 개선할 수 있다.<br>O(2^n)은 각 단계에서 경우의 수가 2배씩 증가하는 경우가 대표적이며 최적화하기 위해서 대표적으로 메모이제이션을 활용한다

```python
# 메모이제이션: 한 번 확인한 데이터를 저장해서 중복확인을 하지않는 방법

# 피보나치 수열 특정 수를 단순 재귀로 찾을 경우 O(2^n)
def fib(n):
  if n <= 1:
    return n
  
  return fib(n - 1) + fib(n - 2)

# 메모제이션 활용 O(n)
memo = {}

def fib(n):
  if n <= 1:
    return n

  if n in memo:
    return memo[n]
  memo[n] = fib(n - 1) + fib(n - 2)
  return memo[n]
# 이런 접근을 동적 계획법이라고 한다
```
<br>모든 O(2^n)을 다 O(n)로 최적화는 불가능하다. O(n^2)정도나 지수시간을 피하기 힘들 수도 있다. <br>반면 O(log n)은 데이터가 2배로 늘어나도 연산횟수는 단 1번만 늘어나며, 아잔탐색이 대표적인 예시다

```python
# 이진 탐색으로 리스트에서 특정값을 찾는 방법
# 이진 탐색: 매번 절반으로 잘라서 값을 찾는 방법

def binary_search(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
    # 중간을 구한다
    mid = (left + right) // 2

    if arr[mid] == target: # 값을 찾았을 경우
      return mid
    elif arr[mid] < target: # 중간이 target보다 작은 경우
      left = mid + 1
    else: # 중간이 target보다 큰 경우
      right mid - 1
  return -1
```
<br>O(n^2)나 O(2^n)를 최적화하기 위한 최소한의 알고리즘은 아래와 같다
1. 같은 계산을 반복할 시 -> 결과저장 (메모제이션/DP)
2. 모든 데이터를 매번 처음부터 찾을 시 -> set, dict, 해시 사용
3. 데이터를 절반씩 제거 가능할 시 -> 이진탐색
4. 중첩 반복을 없앨 수 있을 시 -> 자료구조를 바꾸거나,<br>정렬, 해싱, 투 포인터 등을 활용하여 풀 수 있는 경우가 많음
5. 이미 만들어진 효율적인 알고리즘이 있을 경우<br>
-> 정렬을 직접 구현하지 않고 list.sort() 사용

어떤 상황에서도 적용되는 알고리즘은 없다 <br>프로그래머가 문제를 보고 질문을 하여 알맞은 알고리즘과 자료구조를 사용해야한다 <br>
질문과정에서 자주 등장하는 핵심 도구에는<br> 해싱, 정렬, 이진탐색, 투 포인터, 슬라이딩, 윈도우, 그리디, 분할정보, 동적계획법 등이있다.