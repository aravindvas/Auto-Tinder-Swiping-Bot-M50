from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

usr = "mailme.anonymous2@gmail.com"
pas = "aravindvas1997"


chr_drvr = "D:\Softwares\chromedriver_win32\chromedriver.exe"
drvr = webdriver.Chrome(executable_path=chr_drvr)

drvr.get(url="https://tinder.com/")

time.sleep(5)
but = drvr.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
but.click()
time.sleep(3)
more = drvr.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[1]/div/div[3]/span/button')
more.click()
time.sleep(4)
try:
    fb = drvr.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb.click()
    time.sleep(5)
except NoSuchElementException:
    cls = drvr.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[2]/button')
    cls.click()
    time.sleep(2)
    but = drvr.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
    but.click()
    fb = drvr.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb.click()
    time.sleep(3)

bs_win = drvr.window_handles[0]
fb_win = drvr.window_handles[1]
drvr.switch_to.window(fb_win)
print(drvr.title)

ur = drvr.find_element_by_xpath('//*[@id="email"]')
ps = drvr.find_element_by_xpath('//*[@id="pass"]')
ur.send_keys(usr)
ps.send_keys(pas)
ps.send_keys(Keys.ENTER)

drvr.switch_to.window(bs_win)
print(drvr.title)

time.sleep(15)
loc = drvr.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[1]')
loc.click()
time.sleep(2)
notf = drvr.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[2]')
notf.click()
time.sleep(8)
for i in range(50):
    try:
        # vcn = drvr.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[1]/div[3]/button[2]')
        try:
            lk = drvr.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
            lk.click()
            print("clicked")
            time.sleep(5)
        except NoSuchElementException:
            lk = drvr.find_elements_by_xpath('.button')
            # lk = drvr.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
                                            # '//*[@id="t-828363795"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
            lk.click()
            print("clicked")
            time.sleep(3)
    except ElementClickInterceptedException:
        try:
            match = drvr.find_element_by_css_selector(".itsAMatch a")
            match.click()
        except NoSuchElementException:
            time.sleep(2)

# drvr.quit()