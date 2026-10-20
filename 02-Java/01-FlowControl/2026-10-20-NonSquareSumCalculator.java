// ==============================================================
// ■ 문제 요약
// 정수 N을 입력받아 1부터 N까지의 수 중 제곱수 (1, 4, 9, 16 ...)를 제외한 나머지 수들의 총합을 구하여 출력하는 문제입니다
// ==============================================================
// ■ Algorithm
// 1. 1부터 N까지 순회한다
// 2. 루프변수 i의 제곱근을 구한 뒤, 제곱한 값을 다시 i로 나눈다
// 3. 나누어떨어질 경우 플래그 변수 isSquare에 true 값을 대입한다
// 4. isSquare가 true일 경우 해당 반복은 건너뛰고 false일 경우 count 변수에 i를 더한다
// 5. 순회가 종료된 후 count 값을 출력한다
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 제거
class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int sumNum = 0;

            for (int i = 1; i <= n; i++) {
                boolean isSquare = false;

                int root = (int) Math.sqrt(i);

                if (root * root == i) {
                    isSquare = true;
                }

                if (!isSquare) {
                    sumNum += i;
                }
            }
            System.out.println(sumNum);
        }
    }
}

// ==============================================================