#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/1/14 9:51
from selenium.webdriver import Chrome
from time import sleep

from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("http://dkhcbstest.icwn.cn:800/")
sleep(10)
driver.find_element(By.XPATH, '//*[@placeholder="账号"]').send_keys("admin")
driver.find_element(By.XPATH, '//*[@name="Password"]').send_keys("fintech")
sleep(2)
driver.find_element(By.XPATH, '//*[@ng-click="login()"]').click()
sleep(5)
driver.get(
    "http://dkhcbstest.icwn.cn:800/#/Index/Customer/CustomerList/CustomerList/Detail/false&ee253a9f-49ed-4cb0-af31-1ab5c05cded5")
sleep(5)
customer = driver.find_element(By.XPATH,
                               '//*[@id="content-wrapper"]/div/div/div[2]/div/div/div/div[1]/div/div/div/table/tbody/tr/td[1]/a').text
print(customer)
