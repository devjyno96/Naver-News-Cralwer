from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import csv
# 몇 페이지 크롤링 할지 정해두고
# 각 뉴스는 1부터 10페이지까지의 헤드라인을 긁어온다.
# 그리고 각 헤드라인에 맞는 세션에 저장한다.

# 정치일반 : https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&date=20200511&page=
# 경제일반 : https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=263&sid1=101&date=20200511&page=
# 사회일반 : https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=257&sid1=102&date=20200511&page=
# 생활일반 : https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=245&sid1=103&date=20200511&page=
# 세계일반 : https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=332&sid1=104&date=20200511&page=

# csvfile = csv.writer(file)

# csv 파일을 만드든 코드
page = []
date = []
for i in range(1, 21):
    page.append(i)
session = [(100, 269, "정치"), (101, 263, "경제"), (102, 257, "사회"),
           (103, 245, "생활"), (104, 332, "세계"), ]
# 몇 페이지 크롤링할까 설정
for i in range(20200413, 20200418):
    date.append(i)
 # file = open(i[2]+".txt", 'w', encoding='utf-8-sig', newline='')
 # 처음 저장방식을 txt로 하려고 했었던 시도.
file = open("new_test_10day.csv", 'a', encoding='utf-8-sig', newline='')
# newtrain은 20200504부터 0516
# newtest는  20200406 부터 0418
file.write("제목"+',')
file.write("세션"+'\n')
resultList = []
for d in date:
    print("현재 진행된 날짜 : ", d)
    # 날짜만큼 반복 크롤링
    for i in session:
        # 세션마다 크롤링
        for temp in page:
            # 페이지마다 크롤링
            url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2="+str(i[1])+"&sid1="+str(i[0])+"&date="+str(d)+"&page=" + \
                str(temp)
            res = req.urlopen(url)
            soup = BeautifulSoup(res, "html.parser")
            title_list = soup.select(
                "div.list_body > ul > li > dl > dt:nth-of-type(2) > a ")

            for t in title_list:
                data = t.text.strip().replace(",", "")
                # csv에서 ,로 구분하는데 뉴스 제목에 ',' 때문에 저장방식에 오류 발생 - ',' 삭제
                resultList += [(data, str(i[2]))]

                # file.write(data+","+str(i[2]+"\n"))
            # csvfile.writerow(t+","+str(session[0]))
            resultList = list(set(resultList))  # 중복 제거
            for result in resultList:
                file.write(result[0] + "," + result[1] + "\n")

            resultList = []
            # 다 쓰고 나선 다음 페이지를 위해 resultList를 비워준다.
            # 안그러면 같은 내용을 write한다.