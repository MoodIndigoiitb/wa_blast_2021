from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=D:\\Scrapping\\whatsapp_blast\\chrome_user')
print('Launching Browser...')
browser = webdriver.Chrome(options=options)

browser.get('https://web.whatsapp.com/')
sleep(10)

keepmesignin = browser.find_element_by_tag_name('input')
keepmesignin.click()

