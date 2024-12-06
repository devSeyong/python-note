#문제
#1. 숫자의 승수를 zip으로 맵핑해서 진행하세요.
#2. 숫자를 승수만큼 제곱하여 결과값을 표현해주세요.
#3. 승수한 값이 100이상인 값을 출력하세요.
#4. 승수한 값을 모두 더하세요.
숫자 = [1, 2, 3, 4, 5]
승수 = [2, 2, 2, 3, 3]
# 1.
li = list(zip(숫자, 승수))


def test(x):
    return x >= 100

def test1(x):
    return x[0] ** x[1]


a = list(map(test1, li))
print(a)
b = list(filter(test,a))
print(b)
c = sum(a)
print(c)