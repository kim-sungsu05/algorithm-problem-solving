// ==============================================================
// ■ 문제 요약
// 정수 N을 입력받아, 1부터 k까지의 합 S(k)에 대해 각 단계의 차이인 (S(k) - S(k-1))를 k=1부터 N까지 누적 합산한 최종 결과값을 결과: [값] 형식으로 출력하는 문제입니다.
// S(k)는 1 + ... + k를 의미합니다.
// ==============================================================
// ■ Algorithm
// 정수 N을 입력받아 받아 반복문으로 1 - 0 ... N - N-1까지 순회한다
// 식의 각 항은 1 + .. + N이다
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 제거
class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int inputNum = sc.nextInt();
            int totalResult = 0;

            SequenceSumCalculator calculator = new SequenceSumCalculator();
            
            for (int num = 1; num <= inputNum; num++) {
                int currentSum = calculator.getSumUpTo(num);   // 1 + ... + num 결과를 currentSum에 저장
                int prevSum = calculator.getSumUpTo(num - 1);  // 1 + ... + (num - 1) 결과를 prevSum에 저장
                
                totalResult += (currentSum - prevSum);
            }
            
            System.out.println("결과: " + totalResult);
        }
    }
}

class SequenceSumCalculator {
    /**
     * 1부터 주어진 target 숫자까지의 누적합(S(k))을 계산하여 반환합니다.
     * @param target 누적합을 구할 마지막 숫자
     * @return 1부터 target까지의 합
     */
    public int getSumUpTo(int target) {
        int sum = 0;
        for (int i = 1; i <= target; i++) {
            sum += i;
        }
        return sum;
    }
}

// ==============================================================
// ■ 개선점
// 위의 코드는 호출한 getSumUpTo 메소드에서도 반복을 하고 있기 때문에 2중반복문처럼 O(N^2)의 시간복잡도를 갖는다.
// (S(k) - S(k-1))은 그냥 k이기 때문에 그냥 result += k만해도 문제가 없지만, 객체지향 연습을 위해 클래스를 분리해서 품
// 위 코드는 객체지향 요소를 사용한 코드이긴 하지만, 객체지향적으로 잘 설계된 코드라고 보기는 어렵다
// 상속, 다형성, 캡술화같은 OOP의 핵심 설계 개념을 적극적으로 적재적소에 배치하여 활용해야한다
// 다만, 모든 OOP 개념을 다 사용해야하는 것이 아닌, 문제를 객체와 그 객체의 책임/행동으로 적절하게 모델링하는 것이 핵심이다
// ==============================================================