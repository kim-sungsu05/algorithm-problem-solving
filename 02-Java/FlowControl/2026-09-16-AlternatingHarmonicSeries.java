// ==============================================================
// ■ 문제 요약
// 교대 조화급수(1 - 1/2 + 1/3 - 1/4 + ... +- 1/N)의 합을 구하는 문제로, 
// 입력받은 N까지 인덱스 i의 홀짝 여부에 따라 부호를 번갈아 적용하며 연산한 후 소수점 4자리까지 출력합니다.
// ==============================================================
// ■ Algorithm
// 1. 정수 n을 입력받아 1 - 1/2 + 1/3 - ... ± 1/n 형태로 합한다
// 2. for문으로 더할 때, 홀수면 + 연산, 짝수면 - 연산으로 계산한다
// ==============================================================

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 처음에 1을 두고 for문 안에서 연산을 진행하기 때문에 변수 선언 후, 1로 초기화
        double harmonicSum = 1.0;

        for (int i = 2; i <= n; i++) {
            // 홀수일 경우 + 연산, 짝수일 경우 - 연산
            if (i % 2 == 1) {
                harmonicSum += 1.0 / i;
            } else {
                harmonicSum -= 1.0 / i;
            }
        }

        System.out.printf("합: %.4f\n", harmonicSum);
        sc.close();
    }
}

// ==============================================================
// ■ 개선점
// 루프 일관성 확보: harmonicSum = 0.0 및 i = 1부터 시작하여 첫 항 예외 처리 없이 모든 항을 통일된 로직으로 처리.
// 삼항 연산자 활용 가능: (i % 2 == 1 ? 1 : -1) * (1.0 / i)를 사용하면 if-else 없이 코드 압축 가능.
// 입력 성능 향상 제안: 대용량 데이터 입력 시 Scanner 대신 BufferedReader 사용 권장.
// ==============================================================
// ■ 리펙토링 코드

class Refactoring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 1-1부터 시작해 초기값 특별 처리 없이 일관된 로직으로 계산
        double harmonicSum = 0.0;

        for (int i = 1; i <= n; i++) {
            // 홀수일 경우 + 연산, 짝수일 경우 - 연산
            if (i % 2 == 1) {
                harmonicSum += 1.0 / i;
            } else {
                harmonicSum -= 1.0 / i;
            }
        }

        System.out.printf("합: %.4f\n", harmonicSum);
        sc.close();
    }
}

// ==============================================================
// ■ BufferedReader
// BufferedReader는 입력을 하나씩 가져오지 않고 메모리 버퍼(Buffer)에 모아두었다가 한 번에 읽어오는 텍스트 입력 클래스이다.
// 
// 특징:
// 빠른 속도: 기본 8KB 크기의 버퍼에 데이터를 모아서 가져오므로 CPU & 디스크 접근 횟수가 줄어들어 속도가 매우 빠름.
// String 반환: 모든 입력을 무조건 문자열로 가져오므로, 정수/실수로 쓰려면 Integer.parseInt() 같은 형변환이 필요.
// 예외 처리 필수: 입력 작업 시 반드시 IOException 예외 처리를 해주어야 한다.
// 
// 사용 예시

// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.io.IOException;

   // InputStreamReader로 바이트 스트림을 문자 스트림으로 변환 후 버퍼링
// try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
//     String text = br.readLine();                    한 줄 전체 읽기
//     int number = Integer.parseInt(br.readLine());   읽어온 문자열을 숫자로 변환
// } catch (IOException e) {
//     e.printStackTrace();
// }