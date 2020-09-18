import requests as req
import bs4 as soup
import json
"""
return type

{
"total": 2716447,
"items": [
    {
        "title": "500대 기업, 5년간 M&amp;A투자 59조...<b>삼성전자</b> 10조 최다",
        "originallink": "http://www.consumernews.co.kr/news/articleView.html?idxno=612438",
        "pubDate": "Wed, 16 Sep 2020 09:00:00 +0900"
    },
    ...
"""
def news_crawling(word, day_start = None, day_end = None, sort = 1):
    base_url = "https://search.naver.com/search.naver?where=news"
    result = {"total" : 0, "items" : []}
    base_url += "&query=" + word
    base_url += "&sort=" + str(sort)
    if day_start is not None :
        base_url += "&ds=" + day_start
        base_url += "&de=" + day_end
        base_url += "&nso=so:dd,p:from" + day_start.replace(".", "") + "to" + day_end.replace(".", "") + ",a:all"
        print(base_url)
        
    # &query=(검색어)
    # &sort=(0, 1, 2 : 관련순, 최신, 오래된 순)
    # &ds=(YYYY.MM.DD : 검색 시작)
    # &de=(YYYY.MM.DD : 검색 끝)
    # &nso=so:dd,p:from" + YYYYMMDD + "to" + YYYYMMDD + ",a:all" 기간 검색 조건에 필요햔 query
    # &start=N1 ( N 페이지 접근)

    res = req.get(base_url)
    soup_result = soup.BeautifulSoup(res.text, 'lxml')

    total_article_count = int(soup_result.find(class_="title_desc all_my").find('span').text.split("/")[1][:-1].replace(",", ""))
    result['total'] = total_article_count
    page_count = int(total_article_count / 10)
    if total_article_count % 10 != 0 :
        page_count += 1
     
    print( "page : " + str(page_count)  + " crawling start")
    for page_number in range(page_count):
        res = req.get(base_url + "&start=" + str(page_number) + "1")
        soup_result = soup.BeautifulSoup(res.text, 'html.parser')
        articles = soup_result.find(class_="type01").find_all('li')
        for i in articles :
            item = {}   
            item["title"] = i.find(class_="_sp_each_title")['title']
            item["article_id"] = i.find(class_="_sp_each_title")['onclick'].split('&')[2][25:]
            item["original_link"] = i.find(class_="_sp_each_title")['href']
            item["pub_date"] = [i for i in i.find(class_="txt_inline").text.split("  ") if ' 전' in i or '.' in i][0]
            """
            title = i.find(class_="_sp_each_title")['title']
            article_id = i.find(class_="_sp_each_title")['onclick'].split('&')[2][25:]
            original_url = i.find(class_="_sp_each_title")['href']
            writen_time = [i for i in itim.find(class_="txt_inline").text.split("  ") if ' 전' in i or '.' in i]
            """
            result['items'].append(item)

    print( "page : " + str(page_count)  + " crawling complete")
    return result

if __name__ == "__main__" :
    result = news_crawling("삼성전자", '2020.09.18', '2020.09.18')
    
    with open('test.json', 'w', encoding='utf-8') as f:
        json.dump(result, fp = f, ensure_ascii=False, sort_keys=False, indent=4)