li = list(range(1, 1001))

def filtering(x) -> bool: # 함수 -> bool 은 타입힌트라서 굳이 없어도 함수를 쓰는데 지장은 없음
    if x % 2 == 0 or x % 5 == 0:
        return True
    else:
        return False

new_li = [a for a in li if filtering(a)!= False]

print(new_li)

print(sum(new_li))
print(len(new_li))