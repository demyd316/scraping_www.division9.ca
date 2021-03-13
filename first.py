from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
# from openpyxl import Workbook
# from openpyxl import load_workbook
from os.path import expanduser
from os import path
import os
import csv
import urllib.request
# import xlsxwriter
# import xlrd
import string
# from openpyxl import load_workbook
from csv import writer 
import logging
import threading
import time
def data_scrap(url):
    driver.get(url)
    time.sleep(5)
    name = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/div[2]/h1').text
    sku = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/div[2]/strong').text
    manufacturer = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/div[2]/div[1]/a').text
    description = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/div[2]/div[2]').text
    size1 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[3]/td[2]').text
    size2 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[4]/td[2]').text
    quantity1 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[5]/td[2]').text
    quantity2 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[6]/td[2]').text
    bevel = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[7]/td[2]').text
    finish = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[8]/td[2]').text
    warranty = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[9]/td[2]').text
    installation = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[10]/td[2]').text
    Indoor_Air_Quality = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[11]/td[2]').text
    Radiant_Heat = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[12]/td[2]').text


    Shade = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[2]/tbody/tr[1]/td[2]/a').text
    Performance_Class = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[2]/tbody/tr[3]/td[2]/a').text

    image = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/div[1]/div[1]/a/img').get_attribute('src')

    table_text = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[2]').text
    colour=usage=size=Format=installation_method=space=construction=""
    table_trs = table_text.splitlines()
    # print(table_text)
    for tr in table_trs:
        
        temp1=tr.find("Colour")
        if temp1!=-1:
            colour = tr.rsplit("Colour ")[1]
        
        temp2=tr.find("Usage")
        if temp2!=-1:
            usage = tr.rsplit("Usage ")[1]
            
        temp3=tr.find("Size")
        if temp3!=-1:
            size = tr.rsplit("Size ")[1]
            
        temp4=tr.find("Format")
        if temp4!=-1:
            Format = tr.rsplit("Format ")[1]
            
        temp5=tr.find("Installation Method")
        if temp5!=-1:
            installation_method = tr.rsplit("Installation Method ")[1]
            
        temp6=tr.find("Space")
        if temp6!=-1:
            space = tr.rsplit("Space ")[1]
        
        temp7=tr.find("Construction")
        if temp7!=-1:
            construction = tr.rsplit("Construction ")[1]

    List = [name, sku, manufacturer, description, size1, size2, quantity1, quantity2, bevel, finish, warranty, installation, Indoor_Air_Quality, Radiant_Heat, Shade, Performance_Class, colour, usage, size, Format, installation_method, space, construction, image ]
    with open('sample.csv', 'a', encoding='utf-8-sig', newline='') as f_object: 
        writer_object = writer(f_object) 
        writer_object.writerow(List) 
        f_object.close() 
    time.sleep(1)

driver = webdriver.Chrome()
url = "https://www.division9.ca/en-ca/product/granville-12x24-2"
driver.get(url)


products = driver.find_element_by_id('table-shapes-sizes')
items = products.find_elements_by_tag_name('a')
product_url_list = []
for item in items:
#     item_a_obj = item.find_element_by_class_name('woocommerce-LoopProduct-link')
    product_url_list.append(item.get_attribute('href'))
print(len(product_url_list))
for url in product_url_list:
    data_scrap(url)


