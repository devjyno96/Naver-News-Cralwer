import requests as req
import bs4 as soup

# input
# required / Not required
# word / sort, ds, de
# 검색할 단어/ 정렬 조건, 시작일, 마지막 일

"""
    기간 / pd값
    전체 0
    1일 4
    1주 1 
    1개월 2
    6개월 6
    1년 5 
    1시간 7 
    2시간 8 
    3시간 9 
    4시간 10
    5시간 11
    6시간 12

    custom 3 (없어도 작동함)
    기간을 지정하고 pd를 3 이외의 것으로 두면 pd값이 우선임
    (ex 2010.03.01 을 시작날로 두고 pd를 4로 주면 날자는 사라지고 pd4만 쿼리에 들어가고 오늘부터 1일전 기사만 출력됨)

"""
url = "https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sm=tab_srt&sort=1&ds=2020.09.09&de=2020.09.16"
# https://search.naver.com/search.naver?where=news
# &query=(검색어)&sm=tab_srt
# &sort=(0, 1, 2 : 관련순, 최신, 오래된 순)
# &ds=(YYYY.MM.DD : 검색 시작)
# &de=(YYYY.MM.DD : 검색 끝)"

res = req.get(url)
soup_result = soup.BeautifulSoup(res.text, 'html.parser')

test = soup_result.find(class_="type01").find_all('li')
for item in test :
    testa = item.find('a')
    print(item)
# print(soup_result.find(class_="news mynews section _prs_nws").text)