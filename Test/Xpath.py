from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/Indium Software/PycharmProjects/5_Class/driver/chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//input[@data-testid= 'royal_email']").send_keys("rakesh2290")
driver.find_element_by_xpath("//input[@name= 'pass']").send_keys("Pass")
driver.find_element_by_xpath("//a[text()='Forgotten account?']").click()
