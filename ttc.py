import time #thêm time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

a = '0862693549'
b = 'Application999'
c = 'bobbystanoff'
d = 'Application999'
# a = input("hay nhap tai khoan fb : ")
# b = input("hay nhap nhap khau fb : ")
# c = input("hay nhap tai khoan ttc : ")
# d = input("hay nhap nhap khau ttc : ")

chrome_options = Options()
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1})
driver = webdriver.Chrome(executable_path='/home/bobby/Downloads/chromedriver', chrome_options=chrome_options)

driver.maximize_window()
origin_window = driver.current_window_handle

driver.get('https://www.facebook.com//login') #chạy facebook
time.sleep(1)
driver.find_element_by_id('email').send_keys(a) #UID facebook
time.sleep(1)
driver.find_element_by_id('pass').send_keys(b) #PASS facebook
time.sleep(1)
driver.find_element_by_name('login').click()
time.sleep(3)
driver.get('https://tuongtaccheo.com/') #chạy ttc
time.sleep(2)
driver.execute_script('document.querySelector("#memberModal > div > div > div.modal-footer > div > button").click()')
time.sleep(0.5)
driver.find_element_by_id('name').send_keys(c) #tai khoan ttc
time.sleep(1)
driver.find_element_by_id('password').send_keys(d) #PASS ttc
time.sleep(1)
driver.find_element_by_name('submit').click()
time.sleep(3)
driver.get('https://tuongtaccheo.com/kiemtien/')
##########begining done ###########
controlState = 1
for i in range(10):
    # driver.get('https://tuongtaccheo.com/kiemtien/')
    try:
        ttcRequest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default")))
        ttcRequest.click()
        time.sleep(1)
    except:
        print('cant click?')    
    driver.switch_to.window(driver.window_handles[-1])
    likeButton =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 hpfvmrgz ph5uu5jm b3onmgus iuny7tx3 ipjc6fyt']")))
    likeButton.click()
    time.sleep(0.5)
    driver.close()
    driver.switch_to.window(origin_window)
    time.sleep(1)
    moneyButton = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div[1]/div/div[{controlState}]/div/div/button')     
    moneyButton.click()
    time.sleep(2)
    controlState+= 1
