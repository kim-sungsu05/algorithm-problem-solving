// ==============================================================
// ■ 문제 요약
// 정수 N을 입력받았을 때, 크기순으로 N번째에 위치하는 소수(Prime Number)를 구하여 출력하는 문제입니다.
// ==============================================================
// ■ Algorithm
// 1. 무한반복하여 소수를 계속 구한다
// 2. 소수로 판정될 때마다 count ++
// 3. count == n이 될 경우 현재 소수 출력 후, 종료
// ==============================================================

import java.util.Scanner;

// 파일명 불일치 문제로 public 제거
class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            NthPrimeFinder nth = new NthPrimeFinder(n);
            System.out.println(nth.makePrime());
        }
    }
}

// N번째 소수를 탐색하는 클래스
class NthPrimeFinder {
    private int count = 0;
    private int targetNum;
    private int num = 2; // 1은 소수가 아니므로 2부터 루프를 돌 수 있도록 2저장
    private int primeNumber = 0;

    NthPrimeFinder(int targetNum) {
        this.targetNum = targetNum;
    }

    public int makePrime() {

        while (count != targetNum) { // 현재 입력값까지 소수 카운팅이 되었을 경우 종료 
            boolean isPrime = true;
            
            for (int i = 2; i * i <= num; i++) {
            
                if (num % i == 0) {
                    num++;
                    isPrime = false;
                    break;
                } 
            }
            if (isPrime) {
                primeNumber = num;
                num++;
                count ++;
            }

        }
        return primeNumber;
    }
}

// ==============================================================
// ■ 개선점
// 1. 소수 판별 변수 루프 내부 오염 방지: 원본 코드에서는 소수 검사 for 루프 도중 나누어떨어질 때 num++를 직접 수행하여 다음 소수 판별 검사 범위가 꼬일 위험이 있다.
// 숫자를 늘리는 상태 변화(currentNum++)와 소수 판별 로직(isPrime)을 깔끔히 분리하면 안정성을 확보할 수 있다
// 2. 단일 책임 원칙(SRP) 적용: "소수인지 판별하는 기능(isPrime)"과 "소수를 카운팅하며 N번째 소수를 찾는 기능(getNthPrime)"을 메서드 단위로 격리
// ==============================================================
// ■ 개선 코드

class Refactoring {
    static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            RefactoringNthPrimeFinder finder = new RefactoringNthPrimeFinder();
            int nthPrime = finder.getNthPrime(n);

            System.out.println(nthPrime);
        }
    }
}

/**
 * N번째 소수를 탐색하는 클래스
 */
class RefactoringNthPrimeFinder {

    /**
     * N번째 소수를 찾아 반환합니다.
     */
    public int getNthPrime(int n) {
        if (n <= 0) return 0;

        int count = 0;
        int currentNum = 2;
        int nthPrime = 0;

        while (count < n) {
            if (isPrime(currentNum)) {
                count++;
                nthPrime = currentNum;
            }
            currentNum++;
        }

        return nthPrime;
    }

    /**
     * 단일 정수가 소수인지 판별합니다.
     */
    private boolean isPrime(int number) {
        if (number < 2) return false;

        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

// ==============================================================