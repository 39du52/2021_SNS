from bs4 import BeautifulSoup
from selenium import webdriver

import time, sys, pandas as pd, urllib.request, os
from PIL import Image

print("아마존 닷컴의 분야별 Best Seller 상품 정보 크롤러")

now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

# 분야 이미지 출력
im = Image.open('C:/Users/DELL/Desktop/list.jpg')
im.show()
sec = input("1.분야 번호 선택: ")
cnt = int(input('2.크롤링 건수(1-100 사이): '))
f_dir = input("3.파일을 저장할 폴더명(예 : c:\\temp\\) : ")
print("\n")


if sec == '1':
    sec_name = 'Amazon Devices and Accessories'
elif sec == '2':
    sec_name = 'Amazon Launchpad'
elif sec == '3':
    sec_name = 'Appliances'
elif sec == '4':
    sec_name = 'Apps and Games'
elif sec == '5':
    sec_name = 'Arts and Crafts and Sewing'
elif sec == '6':
    sec_name = 'Audible Books and Originals'
elif sec == '7':
    sec_name = 'Automotive'
elif sec == '8':
    sec_name = 'Baby'
elif sec == '9':
    sec_name = 'Beauty and Personal Care'
elif sec == '10':
    sec_name = 'Books'
elif sec == '11':
    sec_name = 'CDs and Vinyl'
elif sec == '12':
    sec_name = 'Camera and Photo'
elif sec == '13':
    sec_name = 'Cell Phones and Accessories'
elif sec == '14':
    sec_name = 'Clothing and Shoes and Jewelry'
elif sec == '15':
    sec_name = 'Collectible Currencies'
elif sec == '16':
    sec_name = 'Computers and Accessories'
elif sec == '17':
    sec_name = 'Digital Music'
elif sec == '18':
    sec_name = 'Electronics'
elif sec == '19':
    sec_name = 'Entertainment Collectibles'
elif sec == '20':
    sec_name = 'Gift Cards'
elif sec == '21':
    sec_name = 'Grocery and Gourmet Food'
elif sec == '22':
    sec_name = 'Handmade Products'
elif sec == '23':
    sec_name = 'Health and Household'
elif sec == '24':
    sec_name = 'Home and Kitchen'
elif sec == '25':
    sec_name = 'Industrial and Scientific'
elif sec == '26':
    sec_name = 'Kindle Store'
elif sec == '27':
    sec_name = 'Kitchen and Dining'
elif sec == '28':
    sec_name = 'Magazine Subscriptions'
elif sec == '29':
    sec_name = 'Movies and TV'
elif sec == '30':
    sec_name = 'Musical Instruments'
elif sec == '31':
    sec_name = 'Office Products'
elif sec == '32':
    sec_name = 'Patio and Lawn and Garden'
elif sec == '33':
    sec_name = 'Pet Supplies'
elif sec == '34':
    sec_name = 'Prime Pantry'
elif sec == '35':
    sec_name = 'Smart Home'
elif sec == '36':
    sec_name = 'Software'
elif sec == '37':
    sec_name = 'Sports and Outdoors'
elif sec == '38':
    sec_name = 'Sports Collectibles'
elif sec == '39':
    sec_name = 'Tools and Home Improvemen'
elif sec == '40':
    sec_name = 'Toys and Games'
elif sec == '41':
    sec_name = 'Video Games'

query_txt = '아마존닷컴'
query_url = 'https://www.amazon.com/bestsellers?ld=NSGoogle'

os.makedirs(f_dir + '/images')

resultName = s + '-' + query_txt + '-' + sec_name
fileName = f_dir + '/' + resultName
imageName = f_dir + '/images/'

path = "C:/Users/DELL/Desktop/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get(query_url)
time.sleep(1)


if sec == '1':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[1]/a""").click()
elif sec == '2':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[2]/a""").click()
elif sec == '3':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[3]/a""").click()
elif sec == '4':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[4]/a""").click()
elif sec == '5':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[5]/a""").click()
elif sec == '6':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[6]/a""").click()
elif sec == '7':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[7]/a""").click()
elif sec == '8':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[8]/a""").click()
elif sec == '9':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[9]/a""").click()
elif sec == '10':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[10]/a""").click()
elif sec == '11':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[11]/a""").click()
elif sec == '12':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[12]/a""").click()
elif sec == '13':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[13]/a""").click()
elif sec == '14':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[14]/a""").click()
elif sec == '15':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[15]/a""").click()
elif sec == '16':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[16]/a""").click()
elif sec == '17':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[17]/a""").click()
elif sec == '18':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[18]/a""").click()
elif sec == '19':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[19]/a""").click()
elif sec == '20':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[20]/a""").click()
elif sec == '21':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[21]/a""").click()
elif sec == '22':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[22]/a""").click()
elif sec == '23':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[23]/a""").click()
elif sec == '24':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[24]/a""").click()
elif sec == '25':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[25]/a""").click()
elif sec == '26':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[26]/a""").click()
elif sec == '27':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[27]/a""").click()
elif sec == '28':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[28]/a""").click()
elif sec == '29':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[29]/a""").click()
elif sec == '30':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[30]/a""").click()
elif sec == '31':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[31]/a""").click()
elif sec == '32':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[32]/a""").click()
elif sec == '33':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[33]/a""").click()
elif sec == '34':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[34]/a""").click()
elif sec == '35':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[35]/a""").click()
elif sec == '36':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[36]/a""").click()
elif sec == '37':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[37]/a""").click()
elif sec == '38':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[38]/a""").click()
elif sec == '39':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[39]/a""").click()
elif sec == '40':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[40]/a""").click()
elif sec == '41':
    driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[41]/a""").click()

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

for i in range(20):
    driver.execute_script('window.scrollBy(0, 500);')
    time.sleep(0.1)

bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

crew_ranking = []
crew_title = []
crew_price = []
crew_score = []
crew_sat_count = []
crew_store = []
crew_imgs = []

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

reple_result = soup.select('#zg-center-div > #zg-ordered-list')
slist = reple_result[0].find_all('li')

count = 1
while True:
    for li in slist:
        f = open(fileName + '.txt', 'a', encoding='UTF-8')
        f.write("-----------------------------------------------------" + "\n")

        print("-----------------------------------------------------")
        try:
            ranking = li.find('span', class_='zg-badge-text').get_text().replace("#", "")
        except AttributeError:
            ranking = ''
            print(ranking.replace("#", ""))
        else:
            print("1.판매순위:", ranking)
            f.write('1.판매순위:' + ranking + "\n")

        # 제품소개
        try:
            title1 = li.find('div', class_='p13n-sc-truncated').get_text().replace("\n", "")
        except AttributeError:
            title1 = ''
            print(title1.replace("\n", ""))
            f.write('2.제품소개 : ' + title1 + "\n")
        else:
            title2 = title1.translate(bmp_map).replace("\n", "")
            print("2.제품소개 : ", title2.replace("\n", ""))

        f.write('2.제품소개 : ' + title2 + "\n")

        #가격
        try:
            price = li.find('span', 'p13n-sc-price').get_text().replace("\n", "")
        except AttributeError:
            price = ''

        print("3.가격 : ", price.replace("\n", ""))
        f.write('3.가격 : ' + price + "\n")

        try:
            sat_count = li.find('a', 'a-size-small a-link-normal').get_text().replace(",", "")
        except (IndexError, AttributeError):
            sat_count = '0'
            print('4.상품평 수 : ', sat_count)
            f.write('4.상품평 수 :' + sat_count + "\n")
        else:
            print('4.상품평 수 :', sat_count)
            f.write('4.상품평 수 :' + sat_count + "\n")

        #평점
        try:
            score = li.find('span', 'a-icon-alt').get_text()
        except AttributeError:
            score = ' '

        print('5.평점:', score)
        f.write('5.평점:' + score + "\n")

        #이미지
        src = li.find('span', class_='zg-text-center-align').find('img')['src']
        try:
            urllib.request.urlretrieve(src, imageName + str(count) + '.jpg')
            crew_imgs.append(imageName + str(count) + '.jpg')
        except (IndexError, AttributeError):
            continue

        print("-----------------------------------------------------")

        f.close()

        time.sleep(0.1)

        crew_ranking.append(ranking)
        crew_title.append(title2.replace("\n", ''))
        crew_price.append(price.replace("\n", ''))

        try:
            crew_sat_count.append(sat_count)
        except IndexError:
            crew_sat_count.append(0)

        crew_score.append(score)

        if count == cnt:
            break

        count += 1


    if count == cnt:
        break
    else:
        print("페이지 전환")
        driver.find_element_by_xpath("""//*[@id="zg-center-div"]/div[2]/div/ul/li[3]/a""").click()

driver.quit()

amazon_best_seller = pd.DataFrame()
amazon_best_seller['판매순위'] = crew_ranking
amazon_best_seller['제품소개'] = pd.Series(crew_title)
amazon_best_seller['판매가격'] = pd.Series(crew_price)
amazon_best_seller['상품평 갯수'] = pd.Series(crew_sat_count)
amazon_best_seller['상품평점'] = pd.Series(crew_score)

# csv 형태로 저장
amazon_best_seller.to_csv(fileName + '.csv', encoding="utf-8-sig", index=True)

# 엑셀 형태로 저장하기
amazon_best_seller.to_excel(fileName + '.xlsx', index=True)


# 그림추가


print("종료")