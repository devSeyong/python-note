"""
문제: 정수들이 담긴 리스트가 주어질 때, 각 정수를 3배로 만들어 반환하는 함수를 작성하세요.
map() 함수를 사용해야 합니다.

입력 예시: [1, 2, 3, 4, 5]
출력 예시: [3, 6, 9, 12, 15]

요구사항:
1. map() 함수를 사용하세요
2. multiply_by_three 함수를 정의하여 사용하세요
"""
a = [1, 2, 3, 4, 5]

def multiply_by_three(x):
    return x *3
numbers = map(multiply_by_three, a)

print(list(numbers))

"""
1. map,list,lamda를 쓴다
2. 리스트의 각 요소에 2의 배수이면 2를 곱하고, 2의 배수가 아니면 1을 더한다.
3. map과 lamda를 사용하여 한줄로 작성한다.
"""

a = [1,2,3,4,5]
# list(map(lambda x: x * 2 if x % 2 == 0 else x + 1, a ))

def f(x):
    return x*2 if x % 2 == 0 else x + 1

result = list(map(f,a))