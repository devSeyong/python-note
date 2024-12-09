# https://school.programmers.co.kr/learn/courses/30/lessons/120871

l = [] # 저주의 숫자 저장
for i in range(1, 100):
    if i % 3 != 0 and '3' not in str(i):
        l.append(i)

l[39]

def solution(n):
    l = [] # 저주의 숫자 저장
    for i in range(1, 1000):
        if i % 3 != 0 and '3' not in str(i):
            l.append(i)
    return l[n-1]

solution(40)



# https://school.programmers.co.kr/learn/courses/30/lessons/120812

# [1, 2, 3, 3, 3, 4]
# count 메서드를 사용해서 푸는 경우가 많습니다.
# 이러한 문제들은 풀수 있는 내장 모듈이 있습니다.

value = Counter([1, 2, 3, 3, 3, 4])
dir(value)
# value값 가져오기
# most_common

# value.most_common(1)
value.most_common()
# value['3']
value[3]

from collections import Counter

def solution(array):
    if len(array) == 1:
        return array[0]
    arr = Counter(array)
    # print(arr.most_common(1))
    if arr.most_common(1)[0][1] == len(array):
        return array[0]
    one, two = arr.most_common(2)
    if one[1] == two[1]:
        return -1
    return one[0]

# solution([1, 2, 3, 3, 3, 4])
# solution([1, 2, 2, 3, 3, 4])
# solution([]) # 제약 사항에 원소가 1개는 들어가 있다고 합니다.
# solution([1])
solution([2, 2, 2])

###############################
from collections import Counter

def solution(array, n):
    return Counter(array).get(n)