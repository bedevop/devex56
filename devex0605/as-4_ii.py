# AS-4 ii, Igal

from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions as e_Options
from selenium.webdriver.chrome.options import Options as c_Options
from selenium.webdriver.firefox.options import Options as f_Options


# 8
driver_chrome = webdriver.Chrome(executable_path='cd/cd.exe')
url_1 = 'https://www.bettycrocker.com/'
url_2 = 'https://github.com/'
driver_chrome.get(url_1)
cookies = driver_chrome.get_cookies()
pprint(cookies)
driver_chrome.delete_all_cookies()
cookies = driver_chrome.get_cookies()
print('After eating all of the cookies :')
pprint(cookies)

# 9
driver_chrome.get(url_2)
q = driver_chrome.find_element(By.NAME, 'q')
q.send_keys('selenium')
q.send_keys(Keys.ENTER)
driver_chrome.quit()

# 10
dis_ex = '--disable-extensions'
options_c = c_Options()
options_f = f_Options()
options_e = e_Options()
options_c.add_argument(dis_ex)
options_f.add_argument(dis_ex)
options_e.add_argument(dis_ex)
webdriver.Chrome(executable_path='cd/cd.exe', options=options_c)
webdriver.Firefox(executable_path='ff/ff.exe', options=options_f)
Edge(executable_path='ie/msedgedriver.exe', options=options_e)
