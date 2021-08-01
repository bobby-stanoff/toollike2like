import time #thêm time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException        
###################PHAN IN RA MAN HINH#############
print("""\

 __      __         .__   .__                                    
/  \    /  \  ____  |  |  |  |     ____   ____    _____    ____  
\   \/\/   /_/ __ \ |  |  |  |   _/ ___\ /  _ \  /     \ _/ __ \ 
 \        / \  ___/ |  |__|  |__ \  \___(  <_> )|  Y Y  \\  ___/ 
  \__/\  /   \___  >|____/|____/  \___  >\____/ |__|_|  / \___  >
       \/        \/                   \/              \/      \/ 


                    """)
time.sleep(2)
os.system('cls')
# a = trandao1021993@gmail.com 
# b = 21062004huy
# c = trangiahuy21
# d = trangiahuy06
a = input("Account FB : ")
b = input("Pass FB: ")
c = input("Account Tuong Tac Cheo: ")
d = input("Mat Khau Tuong Tac Cheo : ")
os.system('cls')
DELAYTIME = float(input('Time Delay: '))
xuGioiHan = int(input('nhap gioi han xu: '))
os.system('cls')
print("""\


  _____           _  __   __ _        
 |_   _|___  ___ | | \ \ / /(_) _ __  
   | | / _ \/ _ \| |  \ V / | || '_ \ 
   |_| \___/\___/|_|   \_/  |_|| .__/ 
                               |_|    



                    """)
print(' ăn quả nhớ kẻ trồng cây ăn xu thì nhớ mặt tụi tao')                 
time.sleep(3)
os.system('cls')

print('1: job Like')
print('2: job Follow')
SELECTMODE = int(input('Select Job : '))
os.system('cls')
print('Account Fb: ',a)
print('Acc ttc: ' ,c)
print("""\                                               
███████╗███████╗███████╗███████╗███████╗███████╗
╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝  """)




############KHOI DONG SELENIUM########
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1})
driver = webdriver.Chrome(executable_path='/home/bobby/Downloads/chromedriver', options=chrome_options)

driver.maximize_window()
origin_window = driver.current_window_handle

driver.get('https://www.facebook.com/login') #chạy facebook
time.sleep(1)
driver.find_element_by_id('email').send_keys(a) #UID facebook
time.sleep(1)
driver.find_element_by_id('pass').send_keys(b) #PASS facebook
time.sleep(1)
driver.find_element_by_name('login').click()
time.sleep(2)
def check_login():
    try:
        driver.find_element_by_id('ssrb_top_nav_end')
        time.sleep(1)
        
    except NoSuchElementException:
       
        return False
    return True
if check_login():
    print('login thanh cong')
else:
    print('login bi loi')
    sys.exit()
time.sleep(1)
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
# ControlVar = {
#     'jobTong' : 0,
#     'soJobLike' : 0,
#     'soJobFollow' : 0,
#     'accFB' : '',
#     'accTTC' : ''
# }


def ThoatChuongTrinh(message = ''): # dung quan tam lam gi 
    print('----------------------------------')
    print('Account Fb: ',a)
    print('Acc ttc: ' ,c)
    print(message)
    sys.exit()

############ DAY LA JOB LIKE ####################33
def LamJobLike(xuGioiHan):    # tao ham de chon mode like hay follow
    driver.get('https://tuongtaccheo.com/kiemtien/') #link like 

    reLoadJob = driver.find_element_by_id('tailai')  #nut tai lai, het job thi bam de tai them job moi
    
    def JobsListCount(): # ham de dem so job hien co 
        try:   #thu doan code duoi, neu bi loi thi bo qua 
            tempJobsList = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#dspost .col-md-2"))) # dem so job hien co
            return len(tempJobsList) # tra ve so job hien co. vi du co 10 job thi tra ve 10
        except: # neu bi loi doan code tren thi trả ve so 1 
            return 1
    def LikeAction(JobsList): # ham de thuc hien hanh dong like 
        LINKloi = 0
        for i in range(JobsList): # lap tu 1 den so job hien co 
            try:
                ttcRequest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default")))# nut lam job
                ttcRequest.click() # click nut lam job
                time.sleep(1)
            except:
                print('khong the lam job nay') # ko click duoc thi in ra man hinh
                break # in roi thi thoat khoi vong lap
            try:
                driver.switch_to.window(driver.window_handles[-1]) # chuyen sang tab moi mo
                likeButton =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 hpfvmrgz ph5uu5jm b3onmgus iuny7tx3 ipjc6fyt']"))) #nut like
                time.sleep(DELAYTIME) #cho 
                likeButton.click() #nhan nut like
            except: # neu link loi thi thuc hien dong nay
                LINKloi += 1 
                if LINKloi == 10:
                    ThoatChuongTrinh('acc co the bi die')
                print('link loi')
            time.sleep(1)
            driver.close() #dong tab fb
            # errorr heree
            driver.switch_to.window(origin_window) # chuyen ve tab ttc
            time.sleep(1)
            try: 
                moneyButton = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div[1]/div/div[{i+1}]/div/div/button')   #nut nhan tien  
                moneyButton.click() # click nut nhan tien 
            except: #neu bi loi thi in ra 
                print('ko nhan tien')
                break # thoat khoi vong lap
            time.sleep(1)
            soCash = driver.find_element_by_id('soduchinh').text # so xu hien co
            print(f'so xu hien tai: {soCash}') # in ra so xu hien co
            if int(soCash) >= xuGioiHan:
                ThoatChuongTrinh()
            time.sleep(2)

    while True:       #lap 
        Jobslist = JobsListCount() # dem so job truoc roi gan vao bien nay
        LikeAction(Jobslist) # truyen bien nay vao ham thực hien hanh dong like
        reLoadJob.click() # tai lai danh sach job 
###################### HET JOB LIKE ############333

####################DAY LA JOB FOLLOW####################
def LamJobFollow(xuGioiHan):
    driver.get('https://tuongtaccheo.com/kiemtien/subcheo')
    reLoadJob = driver.find_element_by_id('tailai')
    def JobsListCount():
        try:
            tempJobsList = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#dspost .col-md-2")))
            return len(tempJobsList)
        except:
            return 1
    def FollowAction(Jobslist):
        LINKloi = 0
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
                time.sleep(1)         
                followButton1 =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[3]/table/tbody/tr/td[2]/a')))
                time.sleep(1) 
                followButton2 =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[3]/table/tbody/tr/td[3]/a')))
                time.sleep(DELAYTIME)
                if followButton1.text in ['Theo dõi','Follow']:
                    followButton1.click()
                else:
                    followButton2.click()
                time.sleep(1)
            except:
                LINKloi += 1 
                if LINKloi == Jobslist:
                    ThoatChuongTrinh('acc co the bi die')
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
            if int(soCash) >= xuGioiHan:
                ThoatChuongTrinh()
            time.sleep(2)

    while True:       
        Jobslist = JobsListCount()
        FollowAction(Jobslist)
        reLoadJob.click()


##################### HET JOB FOLLOW######################

############PHAN CHINH CUA TOOL############
if SELECTMODE == 1:
    LamJobLike(xuGioiHan)
elif SELECTMODE == 2:
    LamJobFollow(xuGioiHan)








