import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html"
driver.get(url)
time.sleep(2)

# filling the form
data1 = ["2021.08.20. 9:30 AM", "Nora Kiss", "kissnora@gmail.com"]

driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select/option[3]').click()
driver.find_element_by_xpath('//*[@class="next-btn next-btn1"]').click()
time.sleep(2)
driver.find_element_by_class_name("datepicker").send_keys(data1[0])
driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select/option[3]').click()
driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select/option[2]').click()
driver.find_element_by_xpath('//*[@class="next-btn next-btn2"]').click()
time.sleep(2)
driver.find_element_by_name("bf_fullname").send_keys(data1[1])
driver.find_element_by_name("bf_email").send_keys(data1[2])
driver.find_element_by_xpath('//*[@class="submit-btn"]').click()
time.sleep(2)
res_text = driver.find_element_by_xpath('//h2').text

response_text = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can," \
                " which is usually like lightning (Unless we're sailing or eating tacos!)."

# check text of success filling
assert res_text == response_text

driver.close()
driver.quit()

# validation of email address

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html"
driver.get(url)
time.sleep(2)

data2 = ["2021.08.31. 8:42 AM", "Peter Kovacs", "peterkovacsgmail.com"]

driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select/option[3]').click()
driver.find_element_by_xpath('//*[@class="next-btn next-btn1"]').click()
time.sleep(2)
driver.find_element_by_class_name("datepicker").send_keys(data2[0])
driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select/option[3]').click()
driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select/option[2]').click()
driver.find_element_by_xpath('//*[@class="next-btn next-btn2"]').click()
time.sleep(2)
driver.find_element_by_name("bf_fullname").send_keys(data2[1])
driver.find_element_by_name("bf_email").send_keys(data2[2])
driver.find_element_by_xpath('//*[@class="submit-btn"]').click()
time.sleep(2)
error_text = driver.find_element_by_id("bf_email-error").text
message_text = "Please enter a valid email address."

# check text of error message
assert error_text == message_text.upper()

driver.close()
driver.quit()
