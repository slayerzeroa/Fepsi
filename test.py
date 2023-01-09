import re

'''
# ELS -> 이엘스
# DLS -> 디엘스
# IRP -> 아이알피
# RP -> 알픠
# ISA -> 아이에세
# CMA -> 크마
# ELW -> 엘렙
# PRIME -> 픠라임
# WM -> 덥엠
# WRAP -> 덥렙
# Choice&Care -> 초케
# Choice Back -> 초백
# More Care -> 모케
# PLAZA -> 쁠라자
# DB -> 뎁베
# DC -> 뒤씨
# BEST -> 쵀고
# e-book -> 리북
# HTS -> 홈트레이딩서비스
# KB Prestige -> 프레스트지
# Premier -> 푸릐미얼

def cleantext(text):
    cleaned_text = re.sub('ELS', '이엘스', text)
    cleaned_text = re.sub('DLS', '디엘스', cleaned_text)
    cleaned_text = re.sub('IRP', '아이알피', cleaned_text)
    cleaned_text = re.sub('ISA', '아이에세', cleaned_text)
    cleaned_text = re.sub('CMA', '크마', cleaned_text)
    cleaned_text = re.sub('ELW', '엘렙', cleaned_text)
    cleaned_text = re.sub('PRIME', '픠라임', cleaned_text)
    cleaned_text = re.sub('WM', '덥엠', cleaned_text)
    cleaned_text = re.sub('WRAP', '덥렙', cleaned_text)
    cleaned_text = re.sub('Choice&Care', '초케', cleaned_text)
    cleaned_text = re.sub('More Care', '모케', cleaned_text)
    cleaned_text = re.sub('PLAZA', '쁠라자', cleaned_text)
    cleaned_text = re.sub('DB', '뎁베', cleaned_text)
    cleaned_text = re.sub('DC', '뒤씨', cleaned_text)
    cleaned_text = re.sub('BEST', '쵀고', cleaned_text)
    cleaned_text = re.sub('e-book', '리북', cleaned_text)
    cleaned_text = re.sub('HTS', '홈트레이딩서비스', cleaned_text)
    cleaned_text = re.sub('Prestige', '프레스트지', cleaned_text)
    cleaned_text = re.sub('Premier', '푸릐미얼', cleaned_text)
    cleaned_text = re.sub('[a-zA-Z]', '', cleaned_text)  # 영어삭제
    cleaned_text = " ".join(cleaned_text.split())  # 필요없는 공백 삭제
    return cleaned_text

input = input("문자열을 넣어주세요")
print(cleantext(input))
'''


import urllib.request as ureq
from bs4 import BeautifulSoup as bs
import re
from multiprocessing import Pool
import requests
from selenium import webdriver
import numpy as np


class EHHelper:
    @staticmethod
    def EmitTagAndSpecialCh(str):
        str = EHHelper.RemoveTag(str)
        str = EHHelper.RemoveHtmlSpecialCh(str)
        str = EHHelper.RemoveSymbol(str)
        return str
    @staticmethod
    def RemoveTag(src):
        try:
            while True:
                s,e = EHHelper.FindTag(src)
                if s<e:
                    src = src[:s]+src[e+1:]
                else:
                    src = src[:e]+src[e+1:]
        except:
            return src
    @staticmethod
    def FindTag(src):
        s = src.index('<')
        e = src.index('>')
        return s,e
    @staticmethod
    def RemoveSymbol(src):
        dest = ""
        for elem in src:
            if str.isalpha(elem) or str.isspace(elem):
                dest+=elem
        return dest
    @staticmethod
    def RemoveHtmlSpecialCh(src):
        try:
            while True:
                s,e = EHHelper.FindHtmlSpecialCh(src)
                if s<e:
                    src = src[:s]+src[e+1:]
                else:
                    src = src[:e]+src[e+1:]
        except:
            return src
    @staticmethod
    def FindHtmlSpecialCh(src):
        s = src.index('&')
        e = src.index(';')
        return s,e
    @staticmethod
    def MssqlstrToStrKor(src):
        try:
            src = src.encode('ISO-8859-1')
            src = src.decode('euc-kr')
        except:
            return ""
        else:
            return src

'''
def cleantext(text):
    cleaned_text = re.sub('[a-zA-z]', '', text)  # 영어삭제
    cleaned_text = " ".join(cleaned_text.split())  # 필요없는 공백 삭제
    return cleaned_text
'''

# ELS -> 이엘스
# DLS -> 디엘스
# IRP -> 아이알피
# RP -> 알픠
# ISA -> 아이에세
# CMA -> 크마
# ELW -> 엘렙
# PRIME -> 픠라임
# WM -> 덥엠
# WRAP -> 덥렙
# Choice&Care -> 초케
# Choice Back -> 초백
# More Care -> 모케
# PLAZA -> 쁠라자
# DB -> 뎁베
# DC -> 뒤씨
# BEST -> 쵀고
# e-book -> 리북
# HTS -> 홈트레이딩서비스
# KB Prestige -> 프레스트지
# Premier -> 푸릐미얼
def cleantext(text):    # kb 증권 전용 cleaner
    cleaned_text = re.sub('ELS', '이엘스', text)
    cleaned_text = re.sub('DLS', '디엘스', cleaned_text)
    cleaned_text = re.sub('IRP', '아이알피', cleaned_text)
    cleaned_text = re.sub('ISA', '아이에세', cleaned_text)
    cleaned_text = re.sub('CMA', '크마', cleaned_text)
    cleaned_text = re.sub('ELW', '엘렙', cleaned_text)
    cleaned_text = re.sub('PRIME', '픠라임', cleaned_text)
    cleaned_text = re.sub('WM', '덥엠', cleaned_text)
    cleaned_text = re.sub('WRAP', '덥렙', cleaned_text)
    cleaned_text = re.sub('Choice&Care', '초케', cleaned_text)
    cleaned_text = re.sub('More Care', '모케', cleaned_text)
    cleaned_text = re.sub('PLAZA', '쁠라자', cleaned_text)
    cleaned_text = re.sub('DB', '뎁베', cleaned_text)
    cleaned_text = re.sub('DC', '뒤씨', cleaned_text)
    cleaned_text = re.sub('BEST', '쵀고', cleaned_text)
    cleaned_text = re.sub('e-book', '리북', cleaned_text)
    cleaned_text = re.sub('HTS', '홈트레이딩서비스', cleaned_text)
    cleaned_text = re.sub('Prestige', '프레스트지', cleaned_text)
    cleaned_text = re.sub('Premier', '푸릐미얼', cleaned_text)
    cleaned_text = re.sub('ETF', '이퉵', cleaned_text)
    cleaned_text = re.sub('ETN', '이퉨', cleaned_text)
    cleaned_text = re.sub('CFD', '차액거래', cleaned_text)
    cleaned_text = re.sub('[a-zA-Z]', '', cleaned_text)  # 영어삭제
    cleaned_text = " ".join(cleaned_text.split())  # 필요없는 공백 삭제
    return cleaned_text

def Collect(url):  # 내용 수집
    request = ureq.Request(url)
    response = ureq.urlopen(request)
    if response.getcode() != 200:
        return None
    else:
        return response

# selenium
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)
# link list 생성
link_list = []
# link-title 딕셔너리 생성
link_title = {}
def get_link_list():    # 링크 받는 함수
    main_url = 'https://www.kbsec.com/go.able'
    driver.get(main_url)

    html = driver.page_source
    soup = bs(html, 'html.parser')
    # navi > ul > li:nth-child(1) > div > div.colgroup
    # navi > ul > li:nth-child(7) > div > div.colgroup
    # 제대로 가져왔는지 확인
    # 메뉴창의 링크 가져오기
    for i in range(1, 8):
        url_set = "https://www.kbsec.com%s"  # url form 만들어주기
        tags = soup.select('#navi > ul > li:nth-child(%d) > div > div.colgroup'%i)[0].find_all('a')
        for tag in tags:
            link_list.append(tag['href'])
            url_link = url_set % tag['href']  # url 변환
            link_title[url_link] = tag.text
    driver.close()
    return(link_list)

print(get_link_list())
print(link_title)
