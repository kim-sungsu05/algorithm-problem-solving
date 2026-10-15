// ==============================================================
// ■ 문제 요약
// 정수 N을 입력받아, i행에 1부터 i까지의 숫자를 공백 없이 이어 붙여 삼각형 형태로 출력하는 문제입니다
// ==============================================================
// ■ Algorithm
// 스프링 빌더 메서드를 통해 1부터 시작하여 n까지 이어 붙여 출력한다
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 키워드 제거
class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            StringBuilder sb = new StringBuilder();

            for (int num = 1; num <= n; num++) {
                sb.append(num);
                System.out.println(sb);
            }
        }
    }
}

// ==============================================================