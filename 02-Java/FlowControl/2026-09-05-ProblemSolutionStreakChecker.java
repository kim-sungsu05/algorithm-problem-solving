// ==============================================================
// ■ 문제 요약
// 정수를 계속해서 입력받으면서 직전 값(prev)과 연속 횟수(streak)를 추적하여, 
// 같은 정수가 연속으로 3번 입력되는 순간 반복문을 탈출하고 "종료"를 출력합니다 (입력 양식: 공백 또는 줄바꿈으로 구분된 정수열)
// ==============================================================
// ■ Algorithm
// 1. 반복하여 입력값을 입력받는다
// 2. prev가 입력값과 동일한 값인지 비교한다
// 3. 동일한 경우 streak ++
// 4. streak값이 3이 된 경우, 반복 종료 후 '종료' 출력
// ==============================================================

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int prev = Integer.MIN_VALUE;
        int streak = 0;

        while (streak < 3) {

            int num = sc.nextInt();

            if (num == prev) {
                streak++;
            } else {
                // 이전 값과 다르므로 streak을 1로 초기화
                streak = 1;
                // prev값을 현재값으로 초기화
                prev = num;
            }
        }
        System.out.println("종료");
        sc.close();
    }
}
// ==============================================================
// ■ 개선점
// 첫번째 입력처리를 Integer.MIN_VALUE로 할 경우, 첫번째값이 Integer.MIN_VALUE일 경우 streak이 잘못 증가할 수 있는
// 이론적 가능성이 있다. 실무에서는 streak = 0으로 시작하는 대신, 첫번째 값을 루프 전에 읽고 prev = num; streak = 1로 초기화하는
// 패턴을 고려해볼 수 있다
// ==============================================================
// ■ 리펙토링 코드
        // 첫 번째 값을 미리 읽어 prev 초기화 (Integer.MIN_VALUE 엣지케이스 제거)
        // int prev = sc.nextInt();
        // int streak = 1;

        // while (streak < 3) {
        //     int num = sc.nextInt();

        //     if (num == prev) {
        //         streak++;
        //     } else {
        //         // 이전 값과 다르므로 streak을 1로 초기화
        //         streak = 1;
        //         // prev값을 현재값으로 초기화
        //         prev = num;
        //     }
        // }

        // System.out.println("종료");
        // sc.close(); // 리소스 해제