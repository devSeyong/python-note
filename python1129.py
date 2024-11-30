# print() 함수를 사용하여 다음과 같이 출력하세요.
# 출력값 : naver;kakao;sk;samsung

# 정답
print("naver", "kakao", "samsung",sep=";")
#print 함수의 sep 인자로 ";"를 입력하면 출력되는 값들 사이에 한 칸의 공백대신 세미콜론이 출력됩니다.

# print()의 end= 옵션
print("a",end="");print("b",end="");print("c")
# ,end="" 첫번째와 두번째 출력값을 줄바꿈하지않고 이어붙여준다.