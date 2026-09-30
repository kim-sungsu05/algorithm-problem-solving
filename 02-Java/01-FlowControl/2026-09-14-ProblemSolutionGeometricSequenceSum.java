// ==============================================================
// ■ 문제 요약
// 첫째항, 공비, 항의 개수를 입력받아 오버플로우를 방지하기 위한 long 타입을 활용하여 등비수열의 총합을 구해 "합: <합>" 형식으로 출력하는 문제입니다.
// ==============================================================
// ■ Algorithm
// n만큼 반복하여 firstTerm (첫 항)에 commonTerm (공비)를 곱한 등비수열의 합을 출력
// ==============================================================

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long firstTerm = sc.nextLong();
        long commonRatio = sc.nextInt();
        int numTurm = sc.nextInt();

        long sum = 0;

        for (int i = 1; i <= numTurm; i++) {
            sum += firstTerm; // 항의 누적합

            firstTerm *= commonRatio; // 공비를 누적합
        }

        System.out.println("합: " + sum);
        sc.close();
    }
}

// ==============================================================
// ■ 개선점
// 루프 시작 인덱스를 `i=0; i<numTerm` 형태로 바꾸면 Java 관용 표현에 더 부합하다.
// 현재 `i=1; i<=numTerm`도 동작은 같지만 일반적으로 0-based가 선호된다.
// ==============================================================