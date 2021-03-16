# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:46:36 2021

@author: natasjar
"""

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://avi.im/stuff/js-or-no-js.html") #insert website

#you're on your own from here
p_element = driver.find_element_by_id(id_='intro-text')#this only returns the first element with associated html id
print(p_element.text)