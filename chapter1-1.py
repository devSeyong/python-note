'''
주석의 종류는 한 줄 주석 # 과 여러줄 주석 ''''''이 있다.
'''

'''
Docstring(문서화 문자열)

def greet(name):
    """
    이 함수는 이름을 받아 인사 메시지를 반환합니다.
    :param name: 이름 (문자열)
    :return: 인사 메시지
    """
    return f"안녕하세요, {name}님!"

Docstring 작성방법
삼중따옴표(''' ''', """ """)로 문자열을 감싸서 작성할 수 있으며, 주로 함수나 클래스의 목적, 인수, 반환값, 사용 방법 등을 설명하는 데 사용됩니다.
1. 첫 번째 줄에 함수나 클래스의 간단한 설명을 작성합니다. 이 설명은 다른 코드와 구분되도록 빈 줄을 두고 작성해야 합니다.
2. 함수나 메소드가 여러 줄로 된 설명을 제공할 경우, 첫 번째 줄에 간단한 설명을 작성한 후 그 아래에 추가 설명을 넣습니다.
3. 함수의 매개변수나 반환값을 설명할 때는 :param과 :return을 사용하여 각 항목을 명확하게 설명합니다.

Docstring은 필수는 아니지만 매우 유용합니다. 코드를 문서화하고, 협업을 원활하게 하고, 자동화된 문서화 도구와 연계하는 데 매우 중요합니다.
따라서 가능한 한 docstring을 작성하는 것이 좋습니다. 이는 코드의 가독성을 높이고, 나중에 유지보수나 다른 사람과 협업할 때 큰 도움이 됩니다.
'''

'''
변수의 type
a = 10  #int, 정수형
b = 10.1  #float, 실수
c = -1  #float, 실수
d = True  #bool, 논리형(부울형, 참거짓형)
e = 'good'  #str, 문자열
f = '10'  #str, 문자열
g = 'kim'  #str, 문자열
h = 'honggildong'  #str, 문자열
i = 'example'  #str, 문자열
j = 10 + 2j  #complex, 복소수
k = 0b110  #int, 2진법 
l = 0o56  #int, 8진법
m = 0xAC  #int, 16진법
'''

'''
변수의 속성
- 영문과 숫자를 사용할 수 있지만, 숫자로 시작하지는 못합니다.
- 특수문자를 사용할 수는 있으나 실무에서 사용하지 않아요(언더바(_)는 사용합니다.)
- 예약어는 사용하지 않습니다.(if, else if, elif, while, for, etc)
- 대소문자는 구분합니다.
- 언더바로만 사용하거나 언더바로 시작할 수 있습니다.
'''

'''
예약어 종류
True, False, None: 논리값 및 빈값을 나타내는 키워드입니다.
if, else, elif: 조건문을 위한 키워드입니다.
for, while, break, continue: 반복문과 관련된 키워드입니다.
try, except, finally, raise: 예외 처리와 관련된 키워드입니다.
def, return, yield, lambda: 함수 정의 및 반환과 관련된 키워드입니다.
class, import, from, as: 클래스 정의 및 모듈 임포트와 관련된 키워드입니다.
global, nonlocal: 변수의 범위를 명시하는 키워드입니다.
and, or, not: 논리 연산자입니다.
is, in: 객체의 비교 및 포함 여부를 확인하는 키워드입니다.
await, async: 비동기 프로그래밍과 관련된 키워드입니다.
'''

'''
변수의 자료형
- 변수의 자료형은 다양한 데이터를 용도에 맞게 쓰기 위해서
- 파이썬은 변수에 저장된 값을 스스로 판단하여 자료형을 알아내기 때문
[자료형](https://www.notion.so/04df8c7810024f3e96b43d83d7b22584?pvs=21)
'''