// ==============================================================
// ■ 문제 요약
// 첫째항, 공차, 항의 개수를 순서대로 입력받아 반복문을 통해 등차수열의 총합을 계산한 뒤 "합: <합>" 형식으로 출력하는 문제입니다.
// ==============================================================
// ■ Algorithm
// n번만큼 반복하여 term (첫 항)에 a(공차)를 더한 값을 출력한다
// ==============================================================

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int firstTerm = sc.nextInt();
        int commonDiff = sc.nextInt();
        int numTerm = sc.nextInt();

        int sum = 0;

        for (int i = 1; i <= numTerm; i++) {
            sum += firstTerm;

            firstTerm += commonDiff; // 공차를 누적하여 더함
        }

        System.out.println("합: " + sum);
        sc.close();
    }
}

// ==============================================================
// ■ 개선점
// 항의 수가 매우 클 때를 대비해, 수학 공식 `sum = n * (2*firstTerm + (n-1)*commonDiff) / 2`를 활용하는 O(1) 방법도 익혀두면 좋다.
// ==============================================================