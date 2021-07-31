import time #thêm time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# a = '0862693549'
# b = 'Application999'
# c = 'bobbystanoff'
# d = 'Application999'

a = input("hay nhap tai khoan fb : ")
b = input("hay nhap nhap khau fb : ")
c = input("hay nhap tai khoan ttc : ")
d = input("hay nhap nhap khau ttc : ")
DELAYTIME = float(input('nhap thoi gian delay: '))
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1})
driver = webdriver.Chrome(executable_path='/home/bobby/Downloads/chromedriver', chrome_options=chrome_options)

driver.maximize_window()
origin_window = driver.current_window_handle

driver.get('https://www.facebook.com/login') #chạy facebook
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

##########begining done ###########

####################DAY LA JOB FOLLOW####################

driver.get('https://tuongtaccheo.com/kiemtien/subcheo')
reLoadJob = driver.find_element_by_id('tailai')
def JobsListCount():
    try:
        tempJobsList = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#dspost .col-md-2")))
        return len(tempJobsList)
    except:
        return 1
def FollowAction(Jobslist):
    for i in range(Jobslist):
        try:
            ttcRequest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default")))
            tempLink = str(ttcRequest.get_attribute('title'))
            mbasicLink = tempLink.replace('www', 'mbasic').replace("'","")
            ttcRequest.click()
            time.sleep(1)
        except:
            print('khong the lam job nay')
            break
        try:
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(mbasicLink)            
            followButton1 =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[3]/table/tbody/tr/td[2]/a')))
            followButton2 =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[3]/table/tbody/tr/td[3]/a')))
            time.sleep(DELAYTIME)
            if followButton1.text in ['Theo dõi','Follow']:
                followButton1.click()
            else:
                followButton2.click()
            time.sleep(1)
        except:
            print('link loi')
        driver.close()
        driver.switch_to.window(origin_window)
        time.sleep(1)
        try:
            moneyButton = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div/div[1]/div/div[{i+1}]/div/div/button')     
            moneyButton.click()
        except:
            print('ko nhan tien')
            break
        time.sleep(1)
        soCash = driver.find_element_by_id('soduchinh').text
        print(f'so xu hien tai: {soCash}')
        time.sleep(2)

while True:       
    Jobslist = JobsListCount()
    FollowAction(Jobslist)
    reLoadJob.click()
