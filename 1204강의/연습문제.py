'''
for문 while 활용해서 풀어야함
'''

# 입력받은 숫자가 소수인지 판별하세요
# 소수: 1과 자기 자신으로만 나누어지는 수
# 예: 입력 = 7, 출력 = "소수입니다"
num = int(input("Enter a number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")

# 주어진 리스트에서 중복된 숫자를 제거하고 오름차순으로 정렬하세요
# 예: 입력 = [1, 3, 3, 5, 1, 2, 7, 5]
# 출력 = [1, 2, 3, 5, 7]

numbers = [1,3,3,5,1,2,7,5]
result = []
# 중복제거
for num in numbers:
    exits = False
    for unique in result:
        if num == unique:
            exits = True
            break
    if not exits:
        result.append(num)

data = sorted(result)

print(data)

'''a = [1, 3, 3, 5, 1, 2, 7, 5]
x = sorted(set(a))
print(x)'''