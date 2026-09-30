// ==============================================================
// ■ 문제 요약
// 양의 정수 N을 입력받아 % 10과 /= 10 산술 연산을 반복하여 자릿수를 뒤집은 정수를 생성하되, 
// 앞자리의 0은 정수 타입 변환을 통해 자연스럽게 제거하여 출력하는 문제입니다.
// ==============================================================
// ■ Algorithm
// 입력받은 정수를 좌우로 뒤집어 출력
// ==============================================================

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();

        long reversed = 0;

        while (n > 0) {
            
            // 입력받은 정수의 마지막 자릿수를 불러오고, 현재 추출된 자릿수를 가장 앞에 배치
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }

        System.out.println("뒤집은 수: " + reversed);
        sc.close();
    }
}

// ==============================================================
// ■ 개선점
// 원본 값 보존 (temp 활용): n을 직접 소비하지 않고 임시 변수 temp를 사용하여 원본 입력값 데이터의 훼손 방지.
// ==============================================================
// ■ 리펙토링 코드

class Refactoring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();

        // 입력받은 정수를 좌우로 뒤집어 출력
        long reversed = 0;
        long temp = n; // 원본 n값 보존하고, 임시변수로 로직 수행

        while (temp > 0) {
            reversed = reversed * 10 + temp % 10;
            temp /= 10;
        }

        System.out.println("뒤집은 수: " + reversed);
        sc.close();
    }
}
// ==============================================================