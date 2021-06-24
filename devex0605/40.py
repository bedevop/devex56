from selenium import webdriver
from time import sleep


# my_driver = webdriver.Chrome(executable_path='C:/Users/igal.s/Documents/DevEx/4_cd/chromedriver_win32')
my_driver = webdriver.Chrome(executable_path='cd/cd.exe')
my_driver.get("C:/Users/igal.s/Documents/DevEx/4_app/tip_calc/tip_calc/index.html")
bill_amt = my_driver.find_element_by_id('billamt')
bill_amt.send_keys('100')
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element_by_id('peopleamt').send_keys('5')
my_driver.find_element_by_id('calculate').click()

expect = 10
actual = my_driver.find_element_by_id('tip').text
print(actual)

assert int(float(actual)) < expect