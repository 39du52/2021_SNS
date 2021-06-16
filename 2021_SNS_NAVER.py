from bs4 import BeautifulSoup
from selenium import webdriver

import time, pandas as pd

print("네이버 영화 리뷰 정보 수집")

crew_text = input('1. 크롤링 키워드 : ')
cnt = int(input('2. 크롤링 리뷰 개수 : '))
f_dir = input("3. 저장위치 : ")

now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

query_url = 'https://movie.naver.com'
path = "C:/Users/DELL/Desktop/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(query_url)

fileName = f_dir + '/' + crew_text


# 키워드 검색 후 평점으로 이동.
element = driver.find_element_by_id("ipt_tx_srch")
element.send_keys(crew_text)
driver.find_element_by_xpath("""//*[@id="jSearchArea"]/div/button""").click()
driver.find_element_by_xpath("""//*[@id="old_content"]/ul[2]/li/dl/dt/a""").click()

driver.find_element_by_link_text("평점").click()

driver.switch_to.frame('pointAfterListIframe')

crew_score=[]
crew_review=[]
crew_writer=[]
crew_wdate=[]
crew_gonggam=[]
g_crew_gonggam=[]
b_crew_gonggam=[]
crew_dwlist=[]

# 카운트
count = 0
# 페이지 번호
click_count = 1

while True:
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    score_result = soup.find('div', class_='score_result').find('ul')
    slist = score_result.find_all('li')

    for li in slist:

        count += 1

        f = open(fileName + '.txt' , 'a', encoding='UTF-8')

        score = li.find('div', class_='star_score').find('em').get_text().strip()
        crew_score.append(score)

        review = li.find('div', class_='score_reple').find('p').find('span').get_text().strip()
        crew_review.append(review)

        dwlist = li.find('div', class_='score_reple').find_all('em')
        writer = dwlist[0].find('span').get_text()
        crew_writer.append(writer)

        wdate = dwlist[1].text
        crew_wdate.append(wdate)

        gonggam = li.find('div', class_='btn_area').find_all('strong')
        g_gonggam = gonggam[0].text
        g_crew_gonggam.append(g_gonggam)

        b_gonggam = gonggam[1].text
        b_crew_gonggam.append(b_gonggam)

        print("\n")
        print("총 %s 건 중 %s 번째 리뷰 데이터를 수집합니다==============" % (cnt, count))
        print("1.별점:", "*" * int(score), ": ", score)
        print("2.리뷰내용:", review)
        print("3.작성자:", writer)
        print('4.작성일자:', wdate)
        print('5.공감:', g_gonggam)
        print('6.비공감:', b_gonggam)
        print("\n")
        
        f.write("1.별점:" + score + "\n")
        f.write("2.리뷰내용:" + review + "\n")
        f.write("3.작성자:" + writer + "\n")
        f.write("4.작성일자:" + wdate + "\n")
        f.write("5.공감:" + g_gonggam + "\n")
        f.write("6.비공감:" + b_gonggam + "\n")
        
        
        if count == cnt:
            break

    if count == cnt:
        break

    time.sleep(2)

    click_count += 1

    # 페이지 번호 넘기기
    if click_count > cnt:
        break
    else:
        driver.find_element_by_xpath('//*[@id="pagerTagAnchor' + str(click_count) + '"]').click()

    time.sleep(2)


driver.quit()

naver_movie = pd.DataFrame()
naver_movie['별점(평점)']=crew_score
naver_movie['리뷰내용']=crew_review
naver_movie['작성자']=crew_writer
naver_movie['작성일자']=crew_wdate
naver_movie['공감횟수']=g_crew_gonggam
naver_movie['비공감횟수']=b_crew_gonggam

#엑셀, csv 형태로 저장하기
naver_movie.to_excel(fileName + '.xls', index=True)
naver_movie.to_csv(fileName + '.csv', encoding="utf-8-sig", index=True)

print("종료")