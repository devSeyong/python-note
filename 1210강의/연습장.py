# # for를 사용해 1부터 100까지 더하기
# a = 0
# for i in range(1,101):
#     a += i

# print(a)

# # 머쓱이보다 키 큰 사람
# # [149, 180, 192, 170]
# # 167

# a = [149, 180, 192, 170]
# b = 167

# # filter를 사용하여 167보다 큰 키만 걸러냄
# taller_people = filter(lambda h: h > b, a)

# # 필터된 결과의 개수를 셈
# count = len(list(taller_people))

# print(count)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_numbers = [i*3 for i in numbers if i % 2 == 0]

# print(new_numbers)

data = {
    'name' : input("이름 입력: "),
    'age' : int(input("나이 입력: ")),
    'gender' : ['남자']
}


print(data['gender'].append('여자'))
