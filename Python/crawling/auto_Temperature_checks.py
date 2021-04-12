from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

school_name=""
student_name=""
student_birthday=""
student_pw=""
# 위 프로그램 작성자의 현재 학교는 경기도 내에 있으므로
# 학교 선택 과정에서 기본적으로 경기도가 선택됨

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
# 이 프로그램과 같은 폴더안에 chromedriver.exe 파일이 있음
path = "chromedriver.exe"
driver = webdriver.Chrome(path,chrome_options=chrome_options)
driver.set_window_position(800,0)
driver.implicitly_wait(3)
driver.get('https://hcs.eduro.go.kr/')
driver.find_element_by_xpath("//button[@class='loginHome_typeCheck type1']").click()
driver.find_element_by_xpath("//button[@id='btnConfirm2']").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("//button[@class='searchBtn']").click()
select1=Select(driver.find_element_by_xpath("//select[@id='sidolabel']"))
# 여기서 시/도 설정이 가능함
select1.select_by_index(9)
# 여기서 학교급 설정이 가능함
select2=Select(driver.find_element_by_xpath("//select[@id='crseScCode']"))
select2.select_by_index(3)
driver.find_element_by_xpath("//input[@id='orgname']").send_keys(school_name)
driver.find_element_by_xpath("//button[@class='searchBtn']").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div[1]/ul/li/a/p").click()
submit = driver.find_element_by_xpath("//input[@type='submit']")
submit.click()
driver.find_element_by_xpath("//input[@id='user_name_input']").send_keys(student_name)
driver.find_element_by_xpath("//input[@id='birthday_input']").send_keys(student_birthday)
sleep(0.5)
submit = driver.find_element_by_xpath("//input[@type='submit']")
submit.click()
driver.find_element_by_xpath("//input[@type='password']").send_keys(student_pw)
sleep(0.5)
submit = driver.find_element_by_xpath("//input[@type='submit']")
submit.click()
sleep(1.5)
if len(driver.find_element_by_class_name("name").text) > 10:
    print("already checked")
    driver.quit()
else:
    driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div[2]/div/section[2]/div[2]/ul/li/a").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//input[@id='survey_q1a1']").click()
    driver.find_element_by_xpath("//input[@id='survey_q2a1']").click()
    driver.find_element_by_xpath("//input[@id='survey_q3a1']").click()
    print("successfully completed")
    submit = driver.find_element_by_xpath("//input[@type='submit']")
    submit.click()