# 입력 받기
score = int(input("점수를 입력하세요(0-100): "))
attendance = int(input("출석률을 입력하세요(0-100): "))

def calculate_grade(score, attendance):
    # 출석률 체크
    if attendance < 75:
        return "F"
    
    # 점수별 학점 계산
    if score >= 95:
        grade = "A+"
    elif score >= 90:
        grade = "A"
    elif score >= 85:
        grade = "B+"
    elif score >= 80:
        grade = "B"
    elif score >= 75:
        grade = "C+"
    elif score >= 70:
        grade = "C"
    elif score >= 65:
        grade = "D+"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
        
    return grade



# 학점 계산 및 출력
result = calculate_grade(score, attendance)
print(f"당신의 학점은 {result}입니다.")