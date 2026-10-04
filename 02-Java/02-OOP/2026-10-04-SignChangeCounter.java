// ==============================================================
// ■ 문제 요약
// 정수 N을 입력받아 N만큼 공백으로 이루어진 정수를 입력받고 부호가 바뀔 때마다 카운팅 후, 부호가 바뀐 횟수를
// 출력하는 문제입니다. (0은 무시)
// ==============================================================
// ■ Algorithm
// 1. n개의 공백으로 구분된 정수를 입력받아 배열로 변환한다
// 2. 배열을 순회하여 부호가 바뀔 때마다 카운팅한다
// 3. 배열의 0번 인덱스의 부호를 기본 부호로 하고, 부호가 바뀔 때 카운팅, 기본 부호를 변경한다
// 4. 순회가 종료되면 카운팅 값을 출력한다
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 제거
class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int changeSign = 0;
            int currentSign = 0;

            // newArray 배열 생성
            MakeArray mkarr = new MakeArray(n, sc);
            int[] newArray = mkarr.returnArray();

            // 배열 0번째 인덱스로 부호 결정 (1은 +, 0은 -를 의미)
            if (newArray[0] > 0) {
                currentSign = 1;
            } 

            for (int i : newArray) {
                
                int tourSign = 0;

                // 루프변수 부호가 +일 경우는 1, -일 경우는 0
                if (i > 0) {
                    tourSign++;
                }

                // 만약 기본 부호와 다를 경우 기본 변수 새로 갱신, 카운팅
                if (tourSign != currentSign) {
                    currentSign = tourSign;
                    changeSign++;
                }
            }
            System.out.println("부호 변경: " + changeSign);  
        }
    }
}

// n만큼의 정수가 채워진 배열을 반환하는 클래스
class MakeArray {
    private int size;
    private int[] intArray;
    private Scanner sc;

    MakeArray(int size, Scanner sc) {
        this.size = size;
        this.intArray = new int[size];
        this.sc = sc;
    }

    // 배열을 생성
    public int[] returnArray() {
        for (int i = 0; i < size; i++) {
            intArray[i] = sc.nextInt();
        }
        return intArray;
    } 
}

// ==============================================================
// ■ 개선점
// 1. 0번 인덱스 부호를 미리 구하고 반복문에서고 또 0번 인덱스를 자기 자신과 비교하는 불필요한 과정을 1번 인덱스부터
// 순회하도록 하여 연산 효율화
// 2. 부호를 1, -1, 0으로 표현하면 의미가 명확해진다. 
// ==============================================================
// ■ 객체 지향없이 개선 코드

class refactoring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int changeSign = 0;
        int prevSign = 0; // 이전 유효 부호 (1: 양수, -1: 음수, 0: 아직 없음)

        for (int i = 0; i < n; i++) {
            int val = sc.nextInt();

            // 현재 값의 부호 계산 (0이면 건너뜀)
            int curSign = (val > 0) ? 1 : (val < 0) ? -1 : 0;

            if (curSign != 0) {
                // 이전 유효 부호가 있고, 현재 부호와 다르면 변경으로 카운팅
                if (prevSign != 0 && prevSign != curSign) {
                    changeSign++;
                }
                prevSign = curSign; // 이전 부호 갱신
            }
        }

        System.out.println("부호 변경: " + changeSign);
    }
}

// ==============================================================