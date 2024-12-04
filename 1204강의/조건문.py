'''
# black formatter - 코드정렬시켜주는 확장프로그램..쓰면 좋아요
# 파이썬 안티패턴에 대해서 알면 좋아요

1. 주어진 이메일(gmail.com)을 가지고 회원가입
-이메일 형태가 맞는지 확인한다.
2. 주어진 이메일이 db에 있는지 확인

3. 회원가입을 한다.
'''

# 함수를 만들되 두가지의 인자를 받고 
# 두 가지의 인자는 각 문자열이다. 
# 두 가지의 인자에서 a라는 갯수를 세고 
# 그 갯수를 조건문 if,else를 사용해서
# a의 갯수가 더 많으면 True
# b의 갯수가 더 많으면 False
# 같으면 -1을 리턴하라.

def a_count(str1:str, str2:str):
    # 문자열에서 'a'의 갯수를 셈
    a_str1 = str1.count('안')
    a_str2 = str2.count('a')
    
    # 'a'의 갯수가 더 많으면 True 반환
    if a_str1 > a_str2:
        return True
    # 'a'의 갯수가 더 적으면 False 반환
    else:
        if a_str1 < a_str2:
            return False
        # 'a'의 갯수가 같으면 -1 반환
        else:
            return -1
print(a_count("안녕","하세요"))
# ----------------------------------------
# def test(x: str, y: str) -> int | bool:

#     a, b = x.count("a"), y.count("a") # 파이썬은 이렇게 a,b 각각 할당 됩니다.
#     if a == b:
#         return -1

#     if a > b:
#         return True
#     else:
#         return False


# """
# 1. 함수를 만든다. 3개의 인자(문자열)을 받는다.
# 2. 각 인자의 길이를 변수 a, b, c에 저장한다.
# 3. if,elif,else문을 사용하여 
# a,b,c의 길이가 같으면 "모두 같다", 
# 하나만 다르면 "하나만 다르다",
# 모두 다르면 "모두 다르다"를 출력한다.

# """
# def test(x, y, z) :
#     a = len(x), b = len(y), c = len(z)
#     if a == b == c:
#       print("모두 같다")
#     elif a == b or b == c or a == c:
#       print("하나만 다르다")
#     else : 
#       print("모두 다르다")

# test("안녕","안녕","안녕")

# def test(x:str, y:str, z:str) :
    
#     a, b, c = len(x), len(y), len(z)
    
#     if a == b == c:
#       print("모두 같다")
#     elif a == b or b == c or a == c:
#       print("하나만 다르다")
#     else : 
#       print("모두 다르다")

# test("안녕","안녕","안녕")