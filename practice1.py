# 1. basicenglishspeaking.com 크롤링
# https://basicenglishspeaking.com/daily-english-conversation-topics/

import requests # 원하는 서버에 접속하여 거기 있는 html 페이지 가져오는 모듈
from bs4 import BeautifulSoup # html 페이지안에 코드들을 가공하거나 자를수 있는 모듈

site = "https://basicenglishspeaking.com/daily-english-conversation-topics/"
request = requests.get(site) # get방식으로 url을 통해서 접속할 수 있는 지 없는 지
# print(request) # 200: 정상적인 접속, 4xx: 접속 불가

soup = BeautifulSoup(request.text, "html.parser")
div = soup.find("div",{"class": "thrv-columns"})
# print(div)

links = div.findAll("a")

# for link in links:
#     print(link.text)

subject = []

for link in links:
    subject.append(link.text)

# print(len(subject))

print(f"총 {len(subject)}개의 주제를 찾았습니다.")
for i in range(len(subject)):
    print(f"{i+1}: {subject[i]}")