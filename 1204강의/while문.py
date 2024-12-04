'''
1. while  True: 로 무한 루프 생성
2. input() 함수로 사용자로부터 입력을 받아서 변수에 저장
3. 변수를 활용해서 출력
4. if 문으로 변수가 만약 0이면 break로 루프를 빠져나옴 
'''

while True:
    var = int(input("Enter something: "))
    if var == 0:
        break
    print("You entered", var)