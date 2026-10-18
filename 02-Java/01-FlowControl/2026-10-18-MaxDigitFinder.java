// ==============================================================
// ■ 문제 요약
// 양의 정수 N을 입력받아, N을 이루는 각 자릿수 중 가장 큰 숫자를 찾아 자릿수 최댓값: [값] 형태로 출력하는 문제입니다. 
// ==============================================================
// ■ Algorithm
// // 양의 정수 N을 입력받아 N의 자릿수 중 가장 큰 자릿수를 출력한다
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 제거
class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            long n = sc.nextLong();
            long maxDigit = 0;

            while (n > 0) {
                long digit = n % 10;
                n /= 10;

                if (digit > maxDigit) {
                    maxDigit = digit;
                }
            }
            System.out.println("자릿수 최댓값: " + maxDigit);
        }
    }
}

// ==============================================================