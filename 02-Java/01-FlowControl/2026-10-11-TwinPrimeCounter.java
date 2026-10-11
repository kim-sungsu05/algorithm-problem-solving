// ==============================================================
// ■ 문제 요약
// 정수 N을 입력받아, 차이가 2인 두 소수의 쌍((p, p+2), 단 둘 다 소수) 중에서 p+2 <= N을 만족하는 쌍의 총개수를 구하여 출력하는 문제입니다.
// ==============================================================
// ■ Algorithm
// 1. 정수 N을 입력받는다
// 2. 바깥 반복을 N번, 안쪽 반복에서 소수를 탐색한다
// 3. 탐색한 소수의 +2 값도 소수일 경우 count++
// 4. 반복이 끝난 뒤 count 값 출력
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 제거
class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int count = 0;

            for (int i = 2; i <= n - 2; i++) {
                if (selectPrime(i) && selectPrime(i + 2)) {
                    count++;
                }
            }
            System.out.println(count);
        }
    }
    // 소수 탐색 메서드
    public static boolean selectPrime(int num) {
        if (num < 2) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

// ==============================================================
// ■ 개선점
// 입력값이 커질 경우를 대비하여 에라토네스의 체 사용 고려
// ==============================================================