// ==============================================================
// ■ 문제 요약
// 첫 줄에 개수 N을 입력받은 후 0을 제외한 정수를 정확히 N개 입력받아 누적 합을 구하여 
// "합계: <합>" 형식으로 출력하는 문제입니다.
// ==============================================================
// ■ Algorithm
// 1. 정수 n만큼 양의 정수를 입력받는다 (0이 입력됐을 경우 재입력)
// 2. 0이 아닌 정수가 입력됐을 경우 count ++, 0일 경우 continue
// 3. count == n 이 되었을 경우 입력받았던 양의 정수의 합을 출력한다
// ==============================================================

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0, count = 0;

        while (count < n) {
            int inputNum = sc.nextInt();

            if (inputNum == 0) {
                continue; // 입력값이 0일 경우 건너뜀
            } else {
                // 0이 아닌 정수일 경우 count ++, sum에 누적합
                count++;
                sum += inputNum;
            }
        }
        System.out.println("합계: " + sum);
        sc.close();
    }
}

// ==============================================================
// ■ 개선점
// if-else 구조 대신 if (inputNum != 0) { ... } 단일 블록으로 작성하면 더 간결하다.
// sc.close()는 좋은 습관이지만, 실무에서는 try-with-resources(try (Scanner sc = ...) { })를 사용하면 더 안전하게 자원을 관리할 수 있다.
// ==============================================================
// ■ try-with-resources
// 파일, 스캐너, DB연결 처럼 사용 후 반드시 닫아주어야하는 자원을 작업이 끝나면 자동으로 .close(); 해주는 Java7+ 문법이다

class test {
    public static void tryWithResources() {
        try (Scanner sc = new Scanner(System.in)) {
            // 작업 진행
        } // 중괄호가 끝나는 시점에 sc.close()가 자동으로 호출
    }
}

// try (Scanner sc = ...; FileReader fr = ...)처럼 세미콜론(;)을 사용하면 여러 자원을 한 번에 선언하고 순차적으로 자동 해제할 수 있다.

// ==============================================================