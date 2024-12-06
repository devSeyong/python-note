"""
문제: 학생들의 시험 점수가 담긴 딕셔너리를 점수에 따라 정렬하세요.
sorted() 함수와 람다 함수를 함께 사용해야 합니다.

요구사항:
1. sorted() 함수를 사용하세요
2. 람다 함수를 key 매개변수로 사용하세요
3. 점수가 높은 순서대로 정렬하세요(내림차순)
4. 결과는 [(학생이름, 점수)] 형태의 리스트여야 합니다

예시:
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}
결과: [('David', 95), ('Bob', 92), ('Alice', 85), ('Charlie', 78)]

힌트:
- sorted()의 key 매개변수는 정렬 기준을 지정합니다
- 딕셔너리의 .items() 메서드를 사용하면 (키, 값) 쌍을 얻을 수 있습니다
- reverse=True 매개변수로 내림차순 정렬이 가능합니다
"""

scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}
print(scores.items())
result = sorted(scores.items(),key=lambda x : x[1],reverse=True)
print(result)

