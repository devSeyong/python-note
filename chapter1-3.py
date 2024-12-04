'''
숫자 자료형은 크게 정수형, 실수형, 복소수형으로 나뉩니다.
정수형 - int 실수형 - float 복소수형 - complex
'''

'''
문자 자료형 (https://paullabworkspace.notion.site/1-4-105529d99273421b86a6e55d670ac516)
- 순서가 있는 **시퀀스 자료형**입니다.
- 작은 따옴표(' ')나 큰 따옴표(" "), 삼중따옴표(''' ''', """ """)로 감싸는 것도 가능합니다. (삼중따옴표를 사용할 경우에는 줄단위의 문자열을 나타낼 수 있습니다.)
- 작은 따옴표 안에 큰 따옴표, 큰 따옴표 안에 작은 따옴표 사용이 가능합니다.
- 이스케이프 문자도 사용이 가능합니다.

**시퀀스 자료형**
Sequence 즉, 순서가 있는 자료형이라는 뜻으로 각 요소들은 해당하는 Index 값을 갖습니다. 
파이썬에서 가장 많이 사용되는 형태의 자료형이며, 시퀀스 자료형이 가지는 특성을 통하여 인덱싱, 슬라이싱, 반복 등 여러 연산으로 그 활용범위가 넓습니다. 
파이썬에서는 문자열, 리스트, 튜플이 시퀀스 자료형에 해당됩니다. 여기에 딕셔너리, 셋은 포함되지 않으니 주의해주세요.
'''

'''
문자 자료형에서 자주 쓰이는 메서드 (사용되는 형식 : 변수명.메서드명(), 대부분의 문자열 메서드는 새로운 문자열을 반환합니다.) 
- lower( ) / upper( )
lower( )은 전체 데이터를 소문자로 바꿔주는 method이고, upper( )은 전체 데이터를 대문자로 바꿔주는 method입니다.

- find( ) / index( )
find( )와 index( )는 특정 문자열을 찾아서 찾은 문자열의 시작 인덱스를 반환해주는 method입니다.
기본문법
str.find(substring, start=0, end=len(string))
str.index(substring, start=0, end=len(string))
* substring: 찾을 하위 문자열.
* start (선택사항): 검색을 시작할 인덱스 (기본값은 0).
* end (선택사항): 검색을 끝낼 인덱스 (기본값은 문자열의 끝).
두 method에 차이점 : find( )는 문자열을 찾지 못했을때 -1을 반환하지만 index( )는 ValueError가 발생합니다.

- count( )
count( )는 문자열에서 특정 하위 문자열의 등장 횟수를 세는 데 사용하는 method입니다.
기본문법
str.count(substring, start=0, end=len(string))
* substring: 찾고자 하는 하위 문자열 (필수 인자).
* start (선택사항): 검색을 시작할 인덱스 (기본값은 0). 문자열의 특정 위치에서부터 검색을 시작할 수 있습니다.
* end (선택사항): 검색을 끝낼 인덱스 (기본값은 문자열의 끝). 문자열의 특정 위치까지 검색을 제한할 수 있습니다.
기본적으로 문자열 전체를 검색하지만, start와 end 인자를 이용해 검색 범위를 지정할 수 있습니다.
예를 들어,
text = "apple banana apple orange apple"
count_apple_in_range = text.count("apple", 0, 20)
print(count_apple_in_range)  # 2 (0부터 20까지의 범위에서 'apple' 등장 횟수)
count()는 대소문자를 구분하며, 빈 문자열은 길이 + 1의 횟수로 간주됩니다.
예를 들어,
text = "apple"
count_empty = text.count("")
print(count_empty)  # 6 (빈 문자열은 모든 문자 사이와 앞뒤에서 등장하는 것으로 간주됨)

- strip( )
strip( )은 데이터의 양쪽의 공백과 특정 문자를 제거해주는 method입니다.
strip( ) 인수에 따옴표를 쓰고 지우고 싶은 특정 문자나 공백을 입력하면 제거
예를 들어,
text = "xxxppHello, World!xxxpp"
result = text.strip('x.p')
print(result)  # "Hello, World!" (양쪽 끝의 'x,p'가 제거됨)

- replace( )
replace( ) 메서드는 문자열에서 특정 하위 문자열을 다른 문자열로 교체하는 데 사용됩니다.
기본문법
str.replace(old, new, count)
* old: 교체할 하위 문자열.
* new: old를 대체할 새로운 문자열.
* count (선택사항): 교체할 최대 횟수. 기본값은 -1로, 이는 모든 old 문자열을 교체함을 의미합니다.
문자열 내에서 모든 old를 new로 교체합니다.
count 인자를 사용하여 교체 횟수를 제한할 수 있습니다.
원본 문자열은 변경되지 않으며, 새로운 문자열을 반환합니다.
대소문자 구분을 합니다.


'''


