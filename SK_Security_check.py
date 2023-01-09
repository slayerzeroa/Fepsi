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
'''
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)
'''
name_list = ['berkshire','bridgewater','chalie_munger','paul_singer','fisher','gates','lee_lu','icahn','kerrisdale','national_pension','pershing','renaissance','michael_burry','soros','tiger']


berkshire = pd.read_csv("berkshire_hathaway_inc.csv")
bridgewater = pd.read_csv("bridgewater_associates__lp.csv")
chalie_munger = pd.read_csv("daily_journal_corp.csv")
paul_singer = pd.read_csv("elliott_investment_management_l_p_.csv")
fisher = pd.read_csv("fisher_investments_inc.csv")
gates = pd.read_csv("gates_bill_&_melinda_foundation.csv")
lee_lu = pd.read_csv("himalaya_capital_management_llc.csv")
icahn = pd.read_csv("icahn_carl_c_et_al.csv")
kerrisdale = pd.read_csv("kerrisdale_advisers__llc.csv")
national_pension = pd.read_csv("national_pension_service.csv")
pershing = pd.read_csv("pershing_square_capital_management__l_p_.csv")
renaissance = pd.read_csv("renaissance_technologies_llc.csv")
michael_burry = pd.read_csv("scion_asset_management__llc.csv")
soros = pd.read_csv("soros_fund_management_llc.csv")
tiger = pd.read_csv("tiger_management_llc.csv")


con = sqlite3.connect("guru.db")

def cut(df):
    df.columns = df.columns.str.replace(' ', '_')
    del df['Type']


count = 0
for i in name_list:
    cut(eval(f"{i}"))
    eval(f"{i}").to_sql(name_list[count], con)
    count+=1


'''
berkshire
bridgewater
chalie_munger
paul_singer
fisher
gates
lee_lu
icahn
kerrisdale
national_pension
pershing
renaissance
michael_burry
soros
tiger
'''