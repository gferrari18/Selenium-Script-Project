from multiprocessing.connection import wait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd



df = pd.read_excel(r'C:\Users\gusfe\Documents\Python\AutoClicker\nice.xls')

list = []
for x in df.Name:
    list.append(x)
print(list)

TrainTime = input("Enter training time duration: ")
usrname = input("Enter your username: ")
password = input("Enter your password: ")

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)


driver.get('https://www.compliancewire.com/CW3/Standard/Authentication/LogIn')
time.sleep(2) # Let the user actually see something!

search_box = driver.find_element_by_name('UserID')
search_box.send_keys(usrname)

search_box = driver.find_element_by_name("Password")
search_box.send_keys(password)

search_box = driver.find_element_by_name('CompanyCode')
search_box.send_keys('jubl')

search_box.submit()

icon = driver.find_element_by_xpath("//a[@title='User Profile']")
icon.click()

icon = driver.find_element_by_xpath("//a[@title='Administrative View']")
icon.click()

icon = driver.find_element_by_id("HeaderSearchLink")
icon.click()

icon = driver.find_element_by_xpath("//a[@data-search='trainingitems']")
icon.click()

for x in list:
    try:
        wait = WebDriverWait(driver, 10)
        driver.implicitly_wait(2)
        wait.until(EC.visibility_of(driver.find_element_by_id("search-input")))
    except: time.sleep(5)

    icon = driver.find_element_by_id("search-input")
    if x.startswith("PR"):
        x = x[0:9]
    if len(x) >= 48:
        x = x[0:48]
    icon.send_keys(x)
    icon.send_keys(Keys.ENTER)
    time.sleep(2)

    # icon = wait.until(EC.element_to_be_clickable((By.ID,"ActionMenuLink")))
   
    try:
        icon = driver.find_element_by_id("ActionMenuLink")
        icon.click()
    except:
        time.sleep(8)
        try:
            icon = driver.find_element_by_id("ActionMenuLink")
            icon.click()
            print("I tried clicking")
        except:
            fix = input("have you addressed the issue? ")
            icon = driver.find_element_by_id("ActionMenuLink")
            icon.click()


    icon = driver.find_element_by_link_text("Edit Training")
    icon.click()

    driver.switch_to.frame("RecScr")

    timebox = driver.find_element_by_name("CrdDuration")
    timebox.send_keys(Keys.BACKSPACE)
    timebox.send_keys(Keys.BACKSPACE)
    timebox.send_keys(TrainTime)

    s1 = Select(driver.find_element_by_name("CrdDurationUnit"))
    s1.select_by_index(1)

    icon = driver.find_element_by_xpath("//a[@title='Save Changes']")
    icon.click()
    time.sleep(3)






# driver.switch_to.frame("RecScr")

# icon = driver.find_element_by_xpath("//a[@title='User Groups']")
# icon.click()

# action = ActionChains(driver)


# hue = 1
# while hue == 1:
#     icon = driver.find_element_by_css_selector("a[href*='javascript:RemoveUserPopup']")
#     action.move_to_element(icon).click().perform()

#     # action.send_keys(Keys.DOWN).perform()
#     # action.send_keys(Keys.DOWN).perform()
#     time.sleep(2)
#     icon.click()
#     # # action.send_keys(Keys.UP).perform()
#     # action.send_keys(Keys.UP).perform()
#     # action.send_keys(Keys.UP).perform()
#     time.sleep(1)
#     icon2 = driver.find_element_by_xpath("//a[@title='Remove User']")
#     icon2.click()
#     time.sleep(2)



""""
icon = driver.find_element(By.XPATH, "//a[@title='Return to Admin Home']")
icon.click()



iconhard = driver.find_element_by_xpath("//a[contains(@href, 'javascript:RemoveUserPopup')]")
iconhard.click()
"""

time.sleep(5) # Let the user actually see something!
