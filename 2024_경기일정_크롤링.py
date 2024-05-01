# KBO 일정 크롤링
## 2024 UPDATE - 기존에 사용하던 BS 와 다르게 경기 일정은 JS 를 통해 동적으로 생성되기 때문에 Selenium 사용 필요해짐

### 1. 패키지 세팅 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime

driver = webdriver.Chrome()

## 임의의 날짜로 테스트

url = "https://m.sports.naver.com/kbaseball/schedule/index?date=2024-04-30"
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
contents = soup.find_all("li", {"class": "MatchBox_match_item__3_D0Q"})

contentArray = [];

for i in contents:
    item = i.find("div", {"class": "MatchBox_match_area__39dEr"})
    match = item.find_all("div", {"class": "MatchBoxTeamArea_name_info__2IaZV"})
    info = []
    
    for j in match:
        info.append(j.find("strong", {"class": "MatchBoxTeamArea_team__3aB4O"}).string)
    

    if len(info) < 1:
        break;

    contentArray.append({"home": info[1], "away": info[0]})

print(contentArray) #배열길이가 0이면 경기 없음

## 개막 날짜 넣어서 모든 경기 일정 불러오기
startDate = "2024-03-23"
endDate = "2023-11-30" # 임의의 종료 날짜

dates = [];
dateDiff = datetime.date(endDate) - datetime.date(startDate)
timeDelta = datetime.timedelta(days = 1)
for i in range(0, dateDiff):
    dates.append(datetime.date(int(startDate.split('-')[0])) + timeDelta)

print(dates)

