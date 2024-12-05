# 다음 숫자 리스트에서 3의 배수이면서 4의 배수가 아닌 수들의 제곱 값을 구하세요.
numbers = list(range(1, 51))  # 1부터 50까지의 숫자

# 출력 예시: [9, 81, 225, 441, 729, ...]

# 내가 푼 정답
b = numbers = list(range(1, 51))
x = [a**2 for a in b if a % 3 == 0 and a % 4 != 0]
print(x)

# 강사님 정답
a = [x**2 for x in range(1, 51) if x % 3 == 0 and x % 4 != 0]
print(a)


# 다음과 같은 단어 리스트가 있습니다.
words = ['hello', 'world', 'python', 'programming', 'language', 'code', 'list', 'data']

# 아래 조건을 만족하는 새로운 리스트를 만드세요:
# 1. 단어의 길이가 5글자 초과인 것들만 선택
# 2. 선택된 단어들 중 'a' 가 포함된 단어들만 선택
# 3. 최종 선택된 단어들을 대문자로 변환

# 출력 예시: ['LANGUAGE', 'PROGRAMMING']

# 챗지피티4 정답
# 1. 단어의 길이가 5글자 초과인 것들만 선택
long_words = [word for word in words if len(word) > 5]

# 2. 'a'가 포함된 단어들만 선택
words_with_a = [word for word in long_words if 'a' in word]

# 3. 대문자로 변환
final_words = [word.upper() for word in words_with_a]

print(final_words)

# 강사님 정답
words = ['hello', 'world', 'python', 'programming', 'language', 'code', 'list', 'data']

li = [word.upper() for word in words 
      if len(word) > 5 and "a" in word]

print(li) 