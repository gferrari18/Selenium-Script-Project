import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

usrid = input("Enter user ID: ")
usrname = input("Enter your username: ")
password = input("Enter your password: ")

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)


driver.get('https://training.compliancewire.com/CW3/Standard/Authentication/LogIn')
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

icon = driver.find_element_by_xpath("//a[@data-search='users']")
icon.click()


icon = driver.find_element_by_id("search-input")
icon.send_keys(usrid)
icon.send_keys(Keys.ENTER)
time.sleep(7)

driver.switch_to.frame("RecScr")
icon = driver.find_element_by_xpath("//a[@title='User Groups']")
icon.click()
time.sleep(3)

table = driver.find_element(By.ID, "tblGroupList")

action = ActionChains(driver)

for row in table.find_elements(By.TAG_NAME, "tr"):
    print(row)
    for cell in row.find_elements(By.TAG_NAME, "td"):
            pkg = cell.find_element(By.PARTIAL_LINK_TEXT, "A")
            print("1")
            icon = driver.find_element_by_css_selector("a[href*='javascript:RemoveUserPopup']")
            print("2")
            action.move_to_element(icon).click().perform()
            print("3")
            time.sleep(2)
            icon.click()
            time.sleep(1)
            icon2 = driver.find_element_by_xpath("//a[@title='Remove User']")
            icon2.click()
            time.sleep(2)