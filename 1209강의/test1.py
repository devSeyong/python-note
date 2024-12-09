# https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 응급도를 기준으로 진료 순서를 정하려고 합니다.
# 응급도가 높은 순서대로 진료 순서를 정한 배열을 return
def solution(data):
    sorted_emer = sorted(data, reverse=True)
    return [sorted_emer.index(i)+1 for i in data]

solution([3, 76, 24])



# 우편번호 순서대로 정렬해주세요.
우편번호 = {
    '황사평': 1,
    '행복동': 3,
    '헬로월드': 4,
    '사라봉': 2
}

데이터 = ['사라봉', '행복동', '황사평', '헬로월드']
sorted(데이터, key=lambda x:우편번호[x])