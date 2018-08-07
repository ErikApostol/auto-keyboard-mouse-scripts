#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
#import org.openqa.selenium.support.ui.Select;
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(1000) # seconds
driver.get("http://140.136.251.114/Aiamis/Login.aspx")
#assert "Python" in driver.title

#Account
elem = driver.find_element_by_name("ctl00$ContentPlaceHolder$txtAccount")
elem.clear()
elem.send_keys("") # account name
elem.send_keys(Keys.TAB)
assert "No results found." not in driver.page_source

#Password
elem = driver.find_element_by_name("ctl00$ContentPlaceHolder$txtPwd")
elem.clear()
elem.send_keys("") # password
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

#// Get a handle to the open alert, prompt or confirmation
WebDriverWait(driver, 1000).until(EC.alert_is_present())
alert = driver.switch_to.alert;
#// And acknowledge the alert (equivalent to clicking "OK")
alert.accept();

elem = driver.find_element_by_link_text("差勤/日誌填寫");
hover = ActionChains(driver).move_to_element(elem).move_to_element(driver.find_element_by_link_text("專任助理簽到退"));
hover.click().perform();

elem = driver.find_element_by_id("ctl00_ContentPlaceHolder_ddlPlanToday")
Select(elem).select_by_value("500767");

driver.find_element_by_id("ctl00_ContentPlaceHolder_rdSignType_1").click();

elem = driver.find_element_by_id("ctl00_ContentPlaceHolder_txtTodayOther")
elem.clear()
description = u"研究資料整理"
elem.send_keys(description)

driver.find_element_by_id("ctl00_ContentPlaceHolder_btnSignToday").click()

#pause
raw_input()
driver.close()

