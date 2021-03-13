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

    first_table_text = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]').text
    # print(first_table_text)
    size1=size2=quantity1=quantity2=bevel=finish=warranty=installation=Indoor_Air_Quality=Radiant_Heat=""
    first_table_trs = first_table_text.splitlines()
    i=0
    for first_tr in first_table_trs:
        first_temp1=first_tr.find("Size")

        if first_temp1!=-1:        
            i=i+1
        
        first_temp2=first_tr.find("Bevel")
        if first_temp2!=-1:
            bevel = first_tr.rsplit("Bevel ")[1]
            
        first_temp3=first_tr.find("Finish")
        if first_temp3!=-1:
            finish = first_tr.rsplit("Finish ")[1]
            
        first_temp4=first_tr.find("Warranty")
        if first_temp4!=-1:
            warranty = first_tr.rsplit("Warranty ")[1]
            
        first_temp5=first_tr.find("Installation")
        if first_temp5!=-1:
            installation = first_tr.rsplit("Installation ")[1]
            
        first_temp6=first_tr.find("Indoor Air Quality")
        if first_temp6!=-1:
            Indoor_Air_Quality = first_tr.rsplit("Indoor Air Quality ")[1]
        
        first_temp7=first_tr.find("Radiant Heat")
        if first_temp7!=-1:
            Radiant_Heat = first_tr.rsplit("Radiant Heat ")[1]    


    if i==2:
        size1 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[3]/td[2]').text
        size2 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[4]/td[2]').text
        quantity1 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[5]/td[2]').text
        quantity2 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[6]/td[2]').text
    elif i==1:
        size1 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[3]/td[2]').text
        quantity1 = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]/tbody/tr[4]/td[2]').text



    Shade = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[2]/tbody/tr[1]/td[2]/a').text
    Performance_Class = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[2]/tbody/tr[3]/td[2]/a').text

    image = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/div[1]/div[1]/a/img').get_attribute('src')

    table_text = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[2]').text
    Shade=Performance_Class=colour=usage=size=Format=installation_method=space=construction=""
    table_trs = table_text.splitlines()
    # print(table_text)
    for tr in table_trs:
        
        temp11=tr.find("Shade")
        if temp11!=-1:
            Shade = tr.rsplit("Shade ")[1]
        
        temp12=tr.find("Performance Class")
        if temp12!=-1:
            Performance_Class = tr.rsplit("Performance Class ")[1]
        
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
    with open('hardwood.csv', 'a', encoding='utf-8-sig', newline='') as f_object: 
        writer_object = writer(f_object) 
        writer_object.writerow(List) 
        f_object.close() 
    time.sleep(1)

driver = webdriver.Chrome()
url = "https://www.division9.ca/en-ca/search?tgs=hardwood-flooring"
driver.get(url)


products = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div/div[2]/div/div')
items = products.find_elements_by_class_name('item-box')
# print(items)
product_url_list = []
for item in items:
    item_a_obj = item.find_element_by_tag_name('a')
    product_url_list.append(item_a_obj.get_attribute('href'))
print(len(product_url_list))
for url in product_url_list:
    data_scrap(url)


