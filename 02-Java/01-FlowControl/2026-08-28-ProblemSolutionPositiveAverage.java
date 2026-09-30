// ==============================================================
// ■ 문제 요약
// 정수를 계속 입력받다가 음수가 나오면 입력을 종료하고, 
// 그 전까지 입력된 0 이상의 정수들의 평균을 소수점 둘째 자리까지 출력하는 문제입니다.
// ==============================================================
// ■ Algorithm
// // 음수가 입력되기 전까지 양수를 더하면서 반복해서 입력받고, 반복이 끝나면 평균을 출력한다.
// ==============================================================
import java.util.Scanner;

// 파일명과 불일치한 문제로 인해 public 제거
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float sum = 0, count = 0, x;
        // 음수가 입력되기 전까지 양수를 더하면서 반복해서 입력받고, 반복이 끝나면 평균을 출력한다.

        do {
            x = sc.nextInt();

            // do는 무조건 한 번 실행되기 때문에 조건문으로 0 이상 양수만 필터링
            if (x >= 0) {
                sum += x;
                count ++;
            }
        } while (x >= 0);

        // 0보다 작을 경우 '입력 없음' 출력
        if (sum <= 0) {
            System.out.println("입력 없음");
        } else {
            float avgPositive = sum / count;
            System.out.printf("평균: %.2f", avgPositive);
        }
        sc.close();
    }
}

// ==============================================================
// ■ 개선점
// 종료 조건 판단을 sum <= 0이 아닌, count == 0으로 해야한다.
// 0만 여러번 입력되었을 때의 출력값은 0.00이 나와야한다.
// float 대신 double이나 int를 쓰는 것이 정밀도와 관례 측면에서 더 적합하다.
// 변수명 의미 있게 짓기
// ==============================================================
// ■ 리펙토링 코드
// import java.util.Scanner;

// public class Main {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         float sum = 0, count = 0;
//         int totalSum = 0, inputCount = 0;
//         int inpuut;

//         do {
//             inpuut = sc.nextInt();

//             if (inpuut >= 0) {
//                 totalSum += inpuut;
//                 inputCount++;
//             }
//         } while (inpuut >= 0);

//         if (inputCount == 0) {
//             System.out.println("입력 없음");
//         } else {
//             System.out.printf("평균: %.2f", (double) totalSum / inputCount);
//         }
//         sc.close();
//     }
// }
// ==============================================================
