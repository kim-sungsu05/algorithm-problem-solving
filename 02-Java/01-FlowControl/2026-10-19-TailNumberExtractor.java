// ==============================================================
// ■ 문제 요약
// 양의 정수 N과 양의 정수 K를 두 줄에 입력받아 N의 뒤 K자리를 정수로 출력하는 문제입니다. 
// (앞에 붙는 0은 정수형 변환 시 자연스럽게 생략됩니다.)
// ==============================================================
// ■ Algorithm
// 양의 정수 N과 양의 정수 K를 두 줄에 입력받아 N의 뒤 K자리를 정수로 출력.
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 제거
class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            long dividend = 1;

            for (int i = 0; i < k; i++) {
                dividend *= 10; // 제수
            }

            System.out.printf("뒤 %d자리: ", k);
            long digit = n / dividend; // 12
            digit *= dividend;         // 12000
            n %= dividend;             // 345

            System.out.println(n);
        }
    }
}

// ==============================================================
// ■ 개선점
// `digit` 관련 세 줄(나눗셈, 곱셈, 나머지)은 `int result = n % (int)dividend;` 한 줄로 대체할 수 있다.
// `n`은 `int`인데 `dividend`는 `long`으로 선언되어 있어 나머지 연산 시 타입 캐스팅이 발생한다. 문제 범위상 `int`로 통일하거나, `n`도 처음부터 `long`으로 받으면 더 일관성 있다.
// ==============================================================
// ■ 개선 코드

class refactoring {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int k = sc.nextInt();

            // 10^k 계산
            int power = 1;
            for (int i = 0; i < k; i++) {
                power *= 10;
            }

            // 뒤 k자리 = n % 10^k (중간 나눗셈·곱셈 불필요)
            int result = n % power;

            System.out.printf("뒤 %d자리: %d%n", k, result);
        }
    }
}

// ==============================================================