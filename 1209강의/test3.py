# https://school.programmers.co.kr/learn/courses/30/lessons/120896

s = "abcabcadc"
for i in set("abcabcadc"):
    print(i)
    print(s.count(i))
    if s.count(i) == 1:
        print(f'한 번만 등장한 문자: {i}')