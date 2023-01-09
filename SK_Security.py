import urllib.request as ureq
from bs4 import BeautifulSoup as bs
import re
from multiprocessing import Pool
import requests
from selenium import webdriver
import numpy as np
from html_table_parser import parser_functions
import pandas as pd
from time import sleep
import sqlite3

pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)

# selenium
driver = webdriver.Chrome()

# 워렌버핏, 찰리멍거, 르네상스 테크놀로지	히말라야 캐피탈 리루	타이거 매니지먼트	조지 소로스	마이클 버리	칼 아이칸	Kerrisdale Capital Management 삼 아드랭기	켄 피셔	폴 싱어	레이 달리오	국민연금	빌 게이츠	빌 애크먼
name_list = ["berkshire-hathaway-inc", "daily-journal-corp", "renaissance-technologies-llc", "himalaya-capital-management-llc", "tiger-management-llc-ny", "soros-fund-management-llc", "scion-asset-management-llc", "icahn-carl-c-et-al", "kerrisdale-advisers-llc", "fisher-asset-management-llc", "elliott-management-corp", "bridgewater-associates-inc", "national-pension-service", "bill-melinda-gates-foundation-trust", "pershing-square-capital-management-l-p"]

# DB cursor
con = sqlite3.connect("guru.db")

def get_data(url):    # 데이터 받는 함수
    sleep(8)           # 오류 때문에 쉬어주는 시간
    main_url = url      # url 생성
    driver.get(main_url)    # 창 열기
    html = driver.page_source   # html
    soup = bs(html, 'html.parser')  # bs
    countings = soup.find_all('a', {"class":"page-link"})   # 차트 탭 개수를 세기 위한 문법
    countings = str(countings[-2])[30:-4]                   # 차트 탭 개수 필터링
    countings = int(countings)                              # 차트 탭 개수 필터링
    tab_org_data = soup.find("table",{"class":"table table-bordered table-striped table-hover"})    # 첫번째 탭 차트 내용 가져오기
    tab_org_data = str(tab_org_data)
    for click in range(countings-1):        # 클릭 횟수
        sleep(3)
        try:
            x_path = '//*[@id="holdings-by-quarter"]/fieldset/div[2]/div[1]/div[2]/div[2]/ul/li[5]/a'   # xpath
            button = driver.find_element("xpath", x_path)
            driver.execute_script("arguments[0].click();", button)
            tab_data = soup.findall("table", {"class": "current_holdings_table"})  #  n번째 탭 차트 내용 가져오기
            tab_org_data += str(tab_data)        # 데이터 덧붙이기
        except:
            x_path = '//*[@id="holdings-by-quarter"]/fieldset/div[2]/div[1]/div[2]/div[2]/ul/li[4]/a'
            button = driver.find_element("xpath", x_path)
            driver.execute_script("arguments[0].click();", button)
            tab_data = soup.find("table", {"class": "current_holdings_table"})  #  n번째 탭 차트 내용 가져오기
            tab_org_data += str(tab_data)        # 데이터 덧붙이기
    #//*[@id="holdings-by-quarter"]/fieldset/div[2]/div[1]/div[2]/div[2]/ul/li[9]/a
    #//*[@id="holdings-by-quarter"]/fieldset/div[2]/div[1]/div[2]/div[2]/ul/li[5]/a
    #//*[@id="holdings-by-quarter"]/fieldset/div[2]/div[1]/div[2]/div[2]/ul/li[4]/a
    tab_org_data = bs(tab_org_data, 'html.parser')
    return tab_org_data


def count_page(url):    # 차트 페이지 세는 함수
    main_url = url
    driver.get(main_url)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    countings = soup.find_all('a', {"class":"page-link"})
    countings = str(countings[-2])[30:-4]
    driver.close()
    return(countings)

def make_table(data):
    table = parser_functions.make2d(data)
    df = pd.DataFrame(data=table[1:], columns=table[0])
    return df


for i in name_list:
    data = get_data(f"https://whalewisdom.com/filer/{i}#tabholdings_tab_link")                          # 현재 차트 내용 받아오기
    guru_portfolio_table = make_table(data)                                                             # 테이블 생성
    guru_portfolio_table.columns = guru_portfolio_table.columns.str.replace(' ', '_')
    guru_portfolio_table = guru_portfolio_table.drop([guru_portfolio_table.columns[1]], axis=1)
    guru_portfolio_table.drop_duplicates
    #guru_portfolio_table.info()
    con = sqlite3.connect("guru.db")
    guru_portfolio_table.to_sql(f'{i}', con)
