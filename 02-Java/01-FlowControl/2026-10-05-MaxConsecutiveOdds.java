// ==============================================================
// ■ 문제 요약
//  첫 줄에 N, 다음 줄에 N 개의 정수를 받아 연속해서 홀수가 나오는 최대 길이를 출력하는 문제입니다
// ==============================================================
// ■ Algorithm
// 1. n개의 정수를 공백 구분으로 한 줄로 입력받는다
// 2. 홀수가 연속되는 만큼 oddCount ++;
// 3. 짝수가 다음값으로 들어온 경우, oodCount이 최댓값보다 클 경우 최댓값 갱신
// 4. 갱신 후, oddCount를 0으로 초기화 후 반복한다
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 제거
class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            int best = 0;
            int currentOdd = 0;

            // 공백 구분 정수를 순회
            for (int i = 0; i < n; i++) {
                int num = sc.nextInt();

                if (num % 2 != 0) {
                    currentOdd++;
                } else {
                    currentOdd = 0; // 현재 홀수 연속 초기화
                }

                if (currentOdd > best) {
                    // 현재 홀수 연속이 최대 연속보다 클 경우 새로 갱신
                    best = currentOdd;
                }
            }
            System.out.println("최대 홀수 연속: " + best);
        }
    }
}

// ==============================================================
// ■ 개선점
// if (currentOdd > best)로 최댓값을 비교하는 코드를 Math.max() 로 간소화할 수 있다
// ==============================================================