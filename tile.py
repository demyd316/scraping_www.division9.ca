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
    try:
        description = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/div[2]/div[2]').text
    except :
        description = ""
        pass

    Bisque=Construction=Variation=Thickness=Warranty=Absorption_by_Weight=Density=Compressive_Strength=MOHS=Flexural_Strength=""
    Shade=Colour=Usage=Size=Shape=Space=construction=Finish=Collection=""
    div = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div').text
    # print(div)
    x = div.find('Technical Specifications')
    if x!=-1:
        first_table_text = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[1]').text
        first_table_trs = first_table_text.splitlines()
        for first_tr in first_table_trs:
            
            first_temp1=first_tr.find("Bisque")
            if first_temp1!=-1:        
                Bisque = first_tr.rsplit("Bisque ")[1]

            first_temp2=first_tr.find("Construction")
            if first_temp2!=-1:
                Construction = first_tr.rsplit("Construction ")[1]

            first_temp3=first_tr.find("Variation")
            if first_temp3!=-1:
                Variation = first_tr.rsplit("Variation ")[1]

            first_temp4=first_tr.find("Thickness")
            if first_temp4!=-1:
                Thickness = first_tr.rsplit("Thickness ")[1]

            first_temp5=first_tr.find("Warranty")
            if first_temp5!=-1:
                try:
                    Warranty = first_tr.rsplit("Warranty ")[1]
                except :
                    Warranty = ""
                    pass
                    

            first_temp6=first_tr.find("Absorption by Weight")
            if first_temp6!=-1:
                Absorption_by_Weight = first_tr.rsplit("Absorption by Weight ")[1]

            first_temp7=first_tr.find("Density")
            if first_temp7!=-1:
                Density = first_tr.rsplit("Density ")[1]
                
            first_temp8=first_tr.find("Compressive Strength")
            if first_temp8!=-1:
                Compressive_Strength = first_tr.rsplit("Compressive Strength ")[1]
                
            first_temp9=first_tr.find("MOHS")
            if first_temp9!=-1:
                MOHS = first_tr.rsplit("MOHS ")[1]
                
            first_temp10=first_tr.find("Flexural Strength")
            if first_temp10!=-1:
                Flexural_Strength = first_tr.rsplit("Flexural Strength ")[1]
        
        table_text = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table[2]').text
        table_trs = table_text.splitlines()
        for tr in table_trs:
            
            temp=tr.find("Shade")
            if temp!=-1:
                Shade = tr.rsplit("Shade ")[1]        

            temp1=tr.find("Colour")
            if temp1!=-1:
                Colour = tr.rsplit("Colour ")[1]

            temp2=tr.find("Usage")
            if temp2!=-1:
                Usage = tr.rsplit("Usage ")[1]

            temp3=tr.find("Size")
            if temp3!=-1:
                Size = tr.rsplit("Size ")[1]

            temp4=tr.find("Shape")
            if temp4!=-1:
                Shape = tr.rsplit("Shape ")[1]

            temp5=tr.find("Space")
            if temp5!=-1:
                Space = tr.rsplit("Space ")[1]
                
            temp6=tr.find("Construction")
            if temp6!=-1:
                Construction = tr.rsplit("Construction ")[1]

            temp7=tr.find("Gloss Level/Finish")
            if temp7!=-1:
                Finish = tr.rsplit("Gloss Level/Finish ")[1]
                
            temp8=tr.find("Collection")
            if temp8!=-1:
                Collection = tr.rsplit("Collection ")[1]
    else:
        
        table_text = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[2]/div/table').text
        table_trs = table_text.splitlines()
        for tr in table_trs:
            
            temp=tr.find("Shade")
            if temp!=-1:
                Shade = tr.rsplit("Shade ")[1]        

            temp1=tr.find("Colour")
            if temp1!=-1:
                Colour = tr.rsplit("Colour ")[1]

            temp2=tr.find("Usage")
            if temp2!=-1:
                Usage = tr.rsplit("Usage ")[1]

            temp3=tr.find("Size")
            if temp3!=-1:
                Size = tr.rsplit("Size ")[1]

            temp4=tr.find("Shape")
            if temp4!=-1:
                Shape = tr.rsplit("Shape ")[1]

            temp5=tr.find("Space")
            if temp5!=-1:
                Space = tr.rsplit("Space ")[1]
                
            temp6=tr.find("Construction")
            if temp6!=-1:
                Construction = tr.rsplit("Construction ")[1]

            temp7=tr.find("Gloss Level/Finish")
            if temp7!=-1:
                Finish = tr.rsplit("Gloss Level/Finish ")[1]
                
            temp8=tr.find("Collection")
            if temp8!=-1:
                Collection = tr.rsplit("Collection ")[1]


    image = driver.find_element_by_xpath('/html/body/main/div/div/div/div[2]/div[1]/div[1]/div[1]/a/img').get_attribute('src')
    List = [name, sku, manufacturer, description,Bisque,Construction,Variation,Thickness,Warranty,Absorption_by_Weight,Density,Compressive_Strength,MOHS,Flexural_Strength,Shade,Colour,Usage,Size,Shape,Space,construction,Finish,Collection, image ]
    with open('tile.csv', 'a', encoding='utf-8-sig', newline='') as f_object: 
        writer_object = writer(f_object) 
        writer_object.writerow(List) 
        f_object.close() 
    time.sleep(1)

driver = webdriver.Chrome()
url = "https://www.savoia.com/en-ca/search"
driver.get(url)

product_url_list = []
while True:
    time.sleep(6)  
    products = driver.find_element_by_xpath('/html/body/main/div/div/div/div[4]/div/div[2]/div/div')
    items = products.find_elements_by_class_name('item-box')

    for item in items:
        item_a_obj = item.find_element_by_tag_name('a')
        product_url_list.append(item_a_obj.get_attribute('href'))
    try:
        next_btn = driver.find_element_by_class_name('fa-chevron-right')
        next_btn.click()

    except:
        break

print(len(product_url_list))
for url in product_url_list:
    data_scrap(url)


