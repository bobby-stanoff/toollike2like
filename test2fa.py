import time #thêm time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1})
driver = webdriver.Chrome(executable_path='/home/bobby/Downloads/chromedriver', chrome_options=chrome_options)

driver.maximize_window()
origin_window = driver.current_window_handle

driver.get('https://www.facebook.com/login') #chạy facebook
time.sleep(1)
driver.find_element_by_id('email').send_keys('100042274231853') #UID facebook
time.sleep(1)
driver.find_element_by_id('pass').send_keys('biishop1') #PASS facebook
time.sleep(1)
driver.find_element_by_name('login').click()
time.sleep(3)
driver.execute_script("window.open('https://2fa.live/', '_blank')")
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_id('listToken').send_keys('AN7Y CR6R 3UZ4 S2BN DKIX 4RIL 3WN6 75ER')
driver.find_element_by_id('submit').click()
time.sleep(1)
temp2FA = driver.find_element_by_id('output').get_attribute("value")
code2FA = temp2FA.split('|')[-1]
print(code2FA)
driver.close()
driver.switch_to.window(origin_window)
driver.find_element_by_id('approvals_code').send_keys(code2FA)
driver.find_element_by_id('checkpointSubmitButton').click()
time.sleep(1)
driver.find_element_by_id('checkpointSubmitButton').click()