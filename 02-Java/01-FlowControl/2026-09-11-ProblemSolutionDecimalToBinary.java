// ==============================================================
// ■ 문제 요약
// 0 이상의 정수 N을 입력받아 내장 함수 없이 % 2와 /= 2 연산을 반복하여 추출한 비트를 
// 앞쪽에 이어 붙이는 방식으로 10진수를 2진수 문자열로 직접 변환하여 출력하되, 
// 입력값이 0인 경우 "0"이 출력되도록 예외 처리까지 구현하는 문제입니다.
// ==============================================================
// ■ Algorithm
// 1. n이 0보다 클 때까지 반복한다
// 2. 빈 문자열 변수 binary의 뒤에 n의 마지막 자릿수를 붙여나간다
// 3. n의 마지막 자릿수를 제거한다
// ==============================================================

import java.util.Scanner;

// 파일명 불일치로 인해 public 제거
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        String binary = "";
        // n이 0일 경우 0 출력
        if (n == 0) {
            System.out.println(0);
        } else {

            while (n > 0) {
                binary = (n % 2) + binary;
                n /= 2;
            }

            System.out.println(binary);
        }
        sc.close();
    }
}

// ==============================================================
// ■ 개선점
// 효율성 면에서는 String 연결(+)을 반복하면 매번 새 객체가 생성되므로, 
// 입력값이 매우 커질 경우 StringBuilder를 활용하면 더 효율적이다. 
// ==============================================================
// ■ 개선 코드
class Refactor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // n이 0일 경우 0 출력
        if (n == 0) {
            System.out.println("0"); // 숫자 0이 아닌 문자열 "0"으로 출력해 타입 일관성 유지
        } else {
            StringBuilder binary = new StringBuilder(); // String 반복 연결 대신 StringBuilder 사용
            while (n > 0) {
                binary.append(n % 2); // 뒤에 붙이고
                n /= 2;
            }
            System.out.println(binary.reverse()); // reverse()로 올바른 2진수 순서로 변환
        }

        sc.close();
    }
}
// ==============================================================