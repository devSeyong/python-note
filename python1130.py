# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# >> url = "http://sharebook.kr"
# 실행 예: kr

# 정답
# 문자열로 표현된 url에서 `.`을 기준으로 분리합니다. 
# 분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있습니다.
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

# 보충설명
# split('.')으로 분리하면 ['http://sharebook', 'kr']가 됩니다
# 여기서 url_split[-1]은 리스트(배열)의 마지막 요소인 'kr'를 반환하죠.
# 그래서 마지막 요소인 kr이 나오게 되는 것입니다.



# license_plate = "24가 2210"일때 출력값이 2210이 되도록 만드세요.

# 정답
license_plate = "24가 2210"
print(license_plate[-4:])
# 인덱스가 음수라면  -8-7-6-5-4-3-2-1 이런식이에요

# 그래서 license_plate[-4:] 이렇게 표현하면 
# 시작 인덱스인 -4부터 끝까지가 나오게 돼요 
# -4 라고 해서 [-4:] 이게 왼쪽 방향으로가는건 아니구 양수랑 똑같이 오른쪽으로 갑니다
# 그래서 2210 이렇게 나오는 겁니다      