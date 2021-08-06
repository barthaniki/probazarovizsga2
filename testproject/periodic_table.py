from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html"
driver.get(url)

# collect elements
elements = driver.find_elements_by_xpath('//div/ul/li[@class!="empty"]')

# create element list
element_list = []

for element in elements:
    element_list.append(element.get_attribute("data-pos"))
    element_list.append(element.find_element_by_tag_name("span").text)

# read test data file
with open("data.txt", "r") as test_file:
    lines = test_file.readlines()
    test_data = []
    for line in lines:
        test_data.append(line)

# check lists
print(element_list)
print(test_data)

driver.close()
driver.quit()
