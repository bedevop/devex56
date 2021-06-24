# AS-4, Igal
import itertools
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['MOZ_HEADLESS'] = '1'

# 1
sel_d_chrome = webdriver.Chrome(executable_path='cd/cd.exe')
sel_d_firefox = webdriver.Firefox(executable_path='ff/ff.exe')

# sel_d_chrome.get('http://www.walla.co.il/')
# sel_d_firefox.get('http://www.ynet.co.il/')

# 2
title_1 = 'About Version'
url_1 = 'chrome://version/'
try:
    sel_d_chrome.get(url_1)
    get_title = sel_d_chrome.title
    assert title_1 == get_title
    print(get_title + '=' + title_1)
except AssertionError:
    print('Title ' + title_1 + ' not found in ' + url_1)

title_2 = 'VICE - VICE is the definitive guide to enlightening information.'
url_2 = 'https://www.vice.com'
sel_d_firefox.get(url_2)
try:
    get_title = sel_d_firefox.title
    assert title_2 == get_title
    print(get_title + '=' + title_2)
except AssertionError:
    print('Title ' + title_2 + ' not found in ' + url_2)

# 3
sel_d_chrome.quit()

selector = '[type=button]'
url_3 = 'https://getbootstrap.com/docs/5.0/examples/heroes/'
options = webdriver.ChromeOptions()
options.add_argument("headless")
sel_d_chrome = webdriver.Chrome(executable_path='cd/cd.exe', options=options)
sel_d_firefox.get(url_3)
sel_d_chrome.get(url_3)
find_1 = sel_d_chrome.find_elements(By.CSS_SELECTOR, selector)
find_2 = sel_d_firefox.find_elements(By.CSS_SELECTOR, selector)
for button_1, button_2 in itertools.zip_longest(find_1, find_2):
    print('b1:' + button_1.text, 'b2: ' + button_2.text)

# 4, 6
sel_d_chrome.quit()

url_4 = 'https://translate.google.com/?sl=auto&tl=es&op=translate'
sel_d_chrome = webdriver.Chrome(executable_path='cd/cd.exe')
sel_d_chrome.get(url_4)
wb_el_1 = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea'
wb_el_2 = 'er8xn'
wb_el_3 = '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea'
# web_element = sel_d_chrome.find_element(By.XPATH, wb_el_1)
# web_element = sel_d_chrome.find_element(By.CLASS_NAME, wb_el_2)
web_element = sel_d_chrome.find_element(By.CSS_SELECTOR, wb_el_3)
print(web_element)
web_element.send_keys('Hello')

# 5
time.sleep(0.7)
url_5 = 'http://youtube.com'
sel_d_chrome.get(url_5)
sel_d_chrome.find_element_by_id('search').send_keys('Nirvana')
sel_d_chrome.find_element_by_id('search-icon-legacy').click()
time.sleep(0.7)
sel_d_firefox.quit()

# 7
url_6 = 'https://www.facebook.com/'
sel_d_chrome.get(url_6)
sel_d_chrome.find_element(By.ID, 'email').send_keys('bla')
sel_d_chrome.find_element(By.ID, 'pass').send_keys('foo')
sel_d_chrome.find_element(By.NAME, 'login').click()
