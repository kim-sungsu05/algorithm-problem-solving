// ==============================================================
// ■ 문제 요약
// 정수 N을 입력받아 N만큼 공백으로 이루어진 정수를 입력받고 홀수번째 수는 더하고, 짝수번째는 뺀 결과를 출력하는 문제입니다
// ==============================================================
// ■ Algorithm
// for (i=1..N) 입력받으며 i 가 홀수면 +=, 짝수면 -=. "결과: <result>" 출력한다
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 제거
class Main {
    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // 배열 생성 객체 호출
            ArrayReader reader = new ArrayReader(n, sc);
            int[] numbers = reader.readArray();

            // 교차 연산 객체 호출
            AlternatingSumCalculator calculator = new AlternatingSumCalculator(numbers);
            int result = calculator.calculate();

            System.out.println("결과: " + result);
        }
    }
}


// 정수의 공백 입력을 받아 배열로 반환하는 클래스
class ArrayReader {
    private int size;
    private Scanner sc;

    public ArrayReader(int size, Scanner sc) {
        this.size = size;
        this.sc = sc;
    }

    // 객체 상태에 저장하지 않고 생성 즉시 반환하여 불필요한 객체 상태를 만들지 않는다
    public int[] readArray() {
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = sc.nextInt();
        }
        return array;
    }
}


// 홀수 번째 값은 더하고, 짝수 번째 값은 빼는 교차 연산 클래스
class AlternatingSumCalculator {
    private int[] numbers;

    public AlternatingSumCalculator(int[] numbers) {
        this.numbers = numbers;
    }

    public int calculate() {
        int sum = 0;
        
        for (int i = 0; i < numbers.length; i++) {
            // 배열 인덱스가 짝수(0, 2, 4...)면 실제 입력 순서로는 홀수 번째(1, 3, 5...)이므로 덧셈
            if (i % 2 == 0) {
                sum += numbers[i];
            } else {
                sum -= numbers[i];
            }
        }
        
        return sum;
    }
}

// ==============================================================
// ■ 개선점
//전체적으로 클래스별 역할 분리는 잘 되어 있지만, 작은 문제에 비해 클래스를 조금 과하게 나눈 편이므로 상황에 따라 단순화할 수 있다
// (이 문제에서는 객체 지향 공부 목적으로 과도하게 클래스를 나눔)
// 또한 생성 후 변경되지 않는 size, Scanner, numbers는 final로 선언하는 것이 더 적절하다
// ==============================================================