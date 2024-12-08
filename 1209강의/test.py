# 학년, 반, 번호, 이름, 국어, 영어, 수학
# 평균이 높은 순으로 출력하세요.
l = [
    [1, 1, 1, '김철수', 90, 80, 85],
    [3, 1, 2, '박제동', 85, 85, 90],
    [2, 1, 3, '홍길동', 80, 80, 80],
    [5, 1, 4, '이영희', 95, 90, 95],
    [4, 1, 5, '김철수', 90, 80, 85],
]

sorted(l) # 뭘 기준으로 정렬하나요? 맨 앞에 있는 요소를 기준으로 정렬합니다.
sorted(l, key=lambda x: sum(x[4:]), reverse=True) # 나누지 않아도 됩니다.



# 학년, 반, 번호, 이름, 국어, 영어, 수학
# 평균이 높은 순으로 출력하세요. 만약 평균이 같다면 학년 순으로 출력하세요.
l = [
    [1, 1, 1, '김철수', 90, 80, 85],
    [3, 1, 2, '박제동', 90, 80, 85],
    [2, 1, 3, '홍길동', 80, 80, 80],
    [5, 1, 4, '이영희', 90, 80, 85],
    [4, 1, 5, '김철수', 90, 80, 85],
]

sorted(l) # 뭘 기준으로 정렬하나요? 맨 앞에 있는 요소를 기준으로 정렬합니다.
sorted(l, key=lambda x: (sum(x[4:], x[0])), reverse=True) # 나누지 않아도 됩니다.



# 학년, 반, 번호, 이름, 국어, 영어, 수학
# 평균이 높은 순으로 출력하세요. 만약 평균이 같다면 학년 낮은 순으로 출력하세요.
l = [
    [1, 1, 1, '김철수', 90, 80, 85],
    [3, 1, 2, '박제동', 90, 80, 85],
    [2, 1, 3, '홍길동', 80, 80, 80],
    [5, 1, 4, '이영희', 90, 80, 85],
    [4, 1, 5, '김철수', 90, 80, 85],
]

sorted(l) # 뭘 기준으로 정렬하나요? 맨 앞에 있는 요소를 기준으로 정렬합니다.
sorted(l, key=lambda x: (sum(x[4:], -x[0])), reverse=True) # 나누지 않아도 됩니다.
