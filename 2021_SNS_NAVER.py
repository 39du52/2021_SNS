from bs4 import BeautifulSoup
from selenium import webdriver
import time,pandas as pd, urllib.request, os


print("지마켓 Best Seller 상품 정보 추출하기 ")

query_url = "http://corners.gmarket.co.kr/Bestsellers"
#f_dir = "C:/Users/DELL/Desktop/data"

cnt = int(input('1. 크롤링 개수 : '))
f_dir=input('2. 파일을 저장할 폴더명(예 : c:\\temp\\) : ')

# 파일위치, 이름 지정
now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

resultName = s + '-' + 'G마켓'
fileName = f_dir + '/' + resultName
imageName = f_dir + '/images/'

#이미지가 저장될 폴더 생성
os.makedirs(f_dir + '/images')

path = "C:/Users/DELL/Desktop/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get(query_url)
time.sleep(1)

#스크롤 내리기 (이미지 데이터 획득)
for i in range(40):
    driver.execute_script('window.scrollBy(0, 500);')
    time.sleep(0.1)

crew_cnt = 1
crew_ranking = []
crew_title = []
crew_literally_price = []
crew_literally_s_price = []
crew_discount2 = []
imgs = []

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

sale_result = soup.select('div.best-list')
slist = sale_result[1].select('ul > li')


count = 1

while True:
    for li in slist:

        f = open(fileName, 'a', encoding='UTF-8')
        print("-" * 40)
        f.write("-----------------------------------------------------" + "\n")

        try:
            title = li.select('a.itemname')[0].get_text().strip()
        except:
            title = ''
            print(title)
            f.write('2.제품소개:' + title + "\n")
        else:
            print("1.판매순위 : " + str(crew_cnt))
            print("2.제품소개:", title)
            f.write('2.제품소개:' + title + "\n")

        try:
            literally_price = li.find('div', class_='item_price').find('div', 'o-price').get_text().strip()
            print("3.원래가격:", literally_price)
            f.write('3.원래가격:' + literally_price + "\n")
        except AttributeError:
            literally_price = '-'
            print("3.원래가격:", literally_price)
            f.write('3.원래가격:' + literally_price + "\n")

        literally_s_price = li.find('div', class_='item_price').find('div', 's-price').find('strong').get_text().strip()
        print("4.판매가격:", literally_s_price)
        f.write('4.판매가격:' + literally_s_price + "\n")

        #할인율이 존재하지 않을 경우 0% 데이터 추가
        try:
            crew_discount = li.find('div', class_='item_price').find('div', 's-price').find('em').get_text().strip()
            print("5.할인율:", crew_discount)
            f.write('5.할인율:' + crew_discount + "\n")

        except AttributeError:
            crew_discount = '0%'
            print("5.할인율:", crew_discount)
            f.write('5.할인율:' + crew_discount + "\n")

        #이미지
        try:
            getSrc = li.find('img', class_='lazy')['src']
            urllib.request.urlretrieve(getSrc, imageName + str(crew_cnt) + '.jpg')
            imgs.append(imageName + str(crew_cnt) + '.jpg')
        except (IndexError, AttributeError):
            continue


        #배열저장
        crew_ranking.append(crew_cnt)
        crew_title.append(title)
        crew_literally_price.append(literally_price)
        crew_literally_s_price.append(literally_s_price)
        crew_discount2.append(crew_discount)

        if count == cnt:
            break

        count += 1
        crew_cnt += 1


    if count == cnt:
        break

driver.quit()


g_best_seller = pd.DataFrame()

g_best_seller['판매순위'] = crew_ranking
g_best_seller['제품소개'] = pd.Series(crew_title)
g_best_seller['원래가격'] = pd.Series(crew_literally_price)
g_best_seller['판매가격'] = pd.Series(crew_literally_s_price)
g_best_seller['할인율'] = pd.Series(crew_discount2)


# 엑셀 형태로 저장하기
g_best_seller.to_excel(fileName + '.xlsx', index=True)

print("종료")
