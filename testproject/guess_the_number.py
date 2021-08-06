import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"
driver.get(url)
time.sleep(2)

guess_number = driver.find_element_by_xpath('//input[@type="number"]')
guess_btn = driver.find_element_by_xpath('//button[@type="button"]')
restart_btn = driver.find_element_by_xpath('//*[@class="btn btn-warning btn-sm pull-right pull-down"]')
alert_success = driver.find_element_by_xpath('//*[@class="alert alert-success ng-hide"]')
trials = driver.find_element_by_xpath('//*[@class="badge ng-binding"]')

# TC1: find the right number

start = 1
counts = []
for i in range(100):
    guess_number.clear()
    guess_number.send_keys(start)
    guess_btn.click()
    start += 1
    counts.append(i)
    if alert_success.is_displayed():
        break

# # TC2: check number of guesses with inner counter

assert int(trials.text) == (len(counts))

# TC3: check guesses with wrong numbers (out of interval)

wrong_numbers = [-19, 255]

restart_btn.click()
time.sleep(2)

for i in wrong_numbers:
    guess_number.clear()
    guess_number.send_keys(i)
    guess_btn.click()
    time.sleep(2)
    alert_failure = driver.find_element_by_xpath('//*[@class="alert alert-warning"]')
    if i < 1:
        assert alert_failure.text == "Guess higher."
    elif i > 100:
        assert alert_failure.text == "Guess lower."

driver.close()
driver.quit()
