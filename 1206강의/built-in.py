for i in range(10, 101, 10):
    print(i)

x = [10, 20, 30]
for i, j in enumerate(x,1):
    print(i, j)

list(zip('abc','123'))

def 곱하기둘(x):
    return x * 2
# map(함수, 순회가능한_객체)?????
list(map(곱하기둘, '123'))

def 함수(x):
    return x > 5
list(filter(함수, range(10)))

# map 과 filter의 차이점??

def print_args(*args):
    print(args)
    for x in args:
        print(x)

print_args(100, True, 'leehojun')
# *args 가변??

def print_kwargs(a, **kwargs):
    print(a)
    print(kwargs)
    for i in kwargs:
        print(i)

print_kwargs(100, name='leehojun', age='10')
# **kwargs ??? 딕션러니? 이걸 더 많이 사용

def print_args_kwargs(*args, **kwargs):
    print('args:', args)
    for x in args:
        print(x)
    print('kwargs:', kwargs)
    for x in kwargs:
        print(x)
        print(kwargs[x])

print_args_kwargs(100, True, 'leehojun')
print('--------')
print_args_kwargs(score=100, name='leehojun', age='10')
print('--------')
print_args_kwargs(100, True, 'leehojun', score=100, name='leehojun', age='10')
#print('--------')
# print_args_kwargs(100, score=100, True, name='leehojun', 'leehojun', age='10')
# *args, **kwargs 두개 동시 사용??

# 패킹: 여러 값을 하나의 튜플로 묶기
def pack_example(*args):
    print(type(args))  # <class 'tuple'>
    print(args)        # (1, 2, 3)

pack_example(1, 2, 3)

# 언패킹: 시퀀스를 풀어서 전달
numbers = [1, 2, 3]
print(*numbers)  # 1 2 3 (print(1, 2, 3)와 동일)

# 딕셔너리 패킹
def pack_dict_example(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)        # {'name': 'John', 'age': 25}

pack_dict_example(name="John", age=25)

# 딕셔너리 언패킹
person = {'name': 'John', 'age': 25}
user = {'city': 'Seoul', **person}
print(user)  # {'city': 'Seoul', 'name': 'John', 'age': 25}
