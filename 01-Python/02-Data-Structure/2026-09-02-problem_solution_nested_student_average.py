# ==============================================================
# ■ 문제 요약
# 시나리오 번호 t(0~2)를 입력받아 해당 중첩 딕셔너리(data_sets)에서 각 학생의 과목 점수 평균을 소수점 첫째 자리까지 각각 출력한 뒤, 
# 마지막 줄에 전체 학생 평균들의 평균값을 소수점 첫째 자리까지 출력하는 문제입니다.
# ==============================================================
# ■ Algorithm
# 시나리오 딕셔너리에 따라 각 학생의 과목 평균과, 각 학생의 점수 평균의 평균을 구한다
# ==============================================================

data_sets = [
    {
        "윤서": {"수학": 85, "영어": 90, "과학": 78},
        "지우": {"수학": 92, "영어": 88, "과학": 95},
        "민준": {"수학": 65, "영어": 70, "과학": 80},
    },
    {
        "A": {"수학": 90, "영어": 80},
        "B": {"수학": 70, "영어": 80},
    },
    {
        "혼자": {"수학": 80},
    }
]

t = int(input())
students = data_sets[t]

total_avg = 0

# students로 키 순회
for subjects in students:

    # 루프변수 키의 값들의 합
    score_sum = sum(students[subjects].values())

    # 평균을 변수에 할당
    avg = score_sum / len(students[subjects])

    # 가독성을 위해 student_name 변수로 할당 후 출력
    student_name = subjects
    print(f"{student_name}: {avg:.1f}")

    # 총 평균을 위해 total_avg에 저장
    total_avg += avg

print(f"전체 평균: {total_avg / len(students):.1f}")
        
# ==============================================================
# ■ 개선점
# 'for subjects in students:' 에서 루프변수를 'for student_name, subject_score in student.items():'
# 형태로 바꾸면 키, 값을 동시에 받아 students[subject] 처럼 딕셔너리에 다시 접근하지 않아도 된다.
# 'student_name=subject' 처럼 단순 재할당 변수는 삭제하고 루프변수명 자체를 의미있게 짓기
# ==============================================================
# ■ 리펙토링 코드

total_avg = 0

# .items()로 학생명과 과목 딕셔너리를 동시에 받아 가독성 향상
for student_name, subject_scores in students.item():
    
    # 평균을 한 줄로 계산 (중간 변수 score_sum 불필요)
    avg = sum(subject_scores.values()) / len(subject_scores)
    
    print(f"{student_name}: {avg:.1f}")
    total_avg += avg
    
print(f"전체 평균: {total_avg / len(students):.1f}")
    
# ==============================================================