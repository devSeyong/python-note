'''
1. list와 range로 1부터 1000까지의 리스트를 만들기
list(range(1,10))
2. 리스트 컴프리헨션으로 1.에 있는 리스트를 활용해서 새로운 리스트를 만든다.
단, 2의 배수 이고 5의 배수인 경우만 그 리스트에 넣는다.(함수)

3. 2.에서 만든 리스트의 전체 합을 구한다. 그리고 출력

4. 2.에서 만든 리스트의 길이를 구한다. 그리고 출력
'''

# 1번 정답
a = list(range(1,1001))
print(a)

a = []
for i in range(1, 1001):
    a.append(i)
print(a)

a = [i for i in range(1, 1001)]
print(a)

# 2번 정답
x = [n for n in a if n % 2 ==0 and n % 5 ==0]
print(x)


x = []
for n in a:
    if n % 2 == 0 and n % 5 == 0:
        x.append(n)
print(x)

x = []
for n in a:
    if n % 2 == 0 and n % 5 == 0:
        x = x + [n]
print(x)

# 3번 정답
print(sum(x))

# 4번 정답
print(len(x))