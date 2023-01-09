# 출처 : https://western-sky.tistory.com/51

import pandas as pd
import time
from selenium import webdriver

pd.set_option('display.max_rows', 100)

data = pd.DataFrame(data=[], columns=['앱이름','아이디','리뷰','별점','날짜'])

driver = webdriver.Chrome("chromedriver.exe")
url = 'https://play.google.com/store/apps/details?id=com.chucklefish.stardewvalley&hl=ko&gl=US'
driver.get(url)

driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[6]/div/span/span').click()

# 스크롤 다운
def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, 999999999999)")
    time.sleep(1)

scroll_down(driver)

driver.get('https://play.google.com/store/apps/details?id=com.chucklefish.stardewvalley&hl=ko&gl=US&showAllReviews=true')


# 어플 이름 수집
app_name = driver.find_element_by_css_selector('.AHFaub')
app_name.text

# 유저 이름 수집
user_names = driver.find_elements_by_css_selector('.X43Kjb')
user_names[0].text

# 리뷰 수집
reviews = driver.find_elements_by_css_selector('.UD7Dzf')
reviews[0].text


# 별점 수집
star_grades = driver.find_elements_by_xpath('//div[@class="pf5lIe"]/div[@role="img"]')
star_grades[0].get_attribute("aria-label")

# 날짜 수집
dates = driver.find_elements_by_css_selector('.p2TkOb')
dates[0].text


def crawl(driver, data, k):
    # 어플 이름, 아이디, 리뷰, 별점, 날짜 수집
    app_name = driver.find_element_by_css_selector('.AHFaub')
    user_names = driver.find_elements_by_css_selector('.X43Kjb')
    reviews = driver.find_elements_by_css_selector('.UD7Dzf')
    star_grades = driver.find_elements_by_xpath('//div[@class="pf5lIe"]/div[@role="img"]')
    dates = driver.find_elements_by_css_selector('.p2TkOb')
    # k개의 리뷰를 수집합니다.
    for i in range(k):
        tmp = []
        tmp.append(app_name.text)
        tmp.append(user_names[i].text)
        tmp.append(reviews[i].text)
        tmp.append(star_grades[i].get_attribute('aria-label'))
        tmp.append(dates[i].text)

        # 수집한 1명의 리뷰를 결과 프레임에 추가합니다.
        tmp = pd.DataFrame(data=[tmp], columns=data.columns)
        data = pd.concat([data, tmp])

    print(app_name.text + "앱 리뷰 수집 완료")

    return data

# 스크롤 다운을 한 뒤, 크롤링을 해야 인덱스 에러가 발생하지 않음
scroll_down(driver)
data = crawl(driver,data, 10)
# 인덱스 번호를 다시 0부터 리셋합니다.
data.reset_index(inplace=True, drop=True)
data.head()

# 원본 데이터 카피
tmp = data.copy()

# 앞의 별표 5점은 생략
tmp['별점'] = tmp['별점'].apply(lambda x: x[5:])
print(tmp.head(3))

import re

m = re.compile('[0-9][\.0-9]*')

tmp['별점'] = tmp['별점'].apply(lambda x : m.findall(x)[0])
print(tmp.head())
