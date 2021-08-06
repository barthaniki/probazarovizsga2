from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"
driver.get(url)

buttons = driver.find_elements_by_xpath('//label')
chars = driver.find_elements_by_xpath('//li')

# create lists
chars_list = []
chars_teams_list = []
buttons_list = []

for char in chars:
    chars_list.append(char.get_attribute("id"))
    chars_teams_list.append(char.get_attribute("data-teams"))

for button in buttons:
    buttons_list.append(button.get_attribute("for"))

# check Angel's teams
if chars_list[0]:
    assert buttons_list[0] in chars_teams_list[0]
    assert buttons_list[1] in chars_teams_list[0]
    assert buttons_list[2] in chars_teams_list[0]
    assert buttons_list[3] in chars_teams_list[0]

# check Magneto's teams
if chars_list[6]:
    assert buttons_list[0] not in chars_teams_list[6]
    assert buttons_list[1] not in chars_teams_list[6]
    assert buttons_list[2] not in chars_teams_list[6]
    assert buttons_list[3] in chars_teams_list[6]

# check Psylocke's teams
if chars_list[9]:
    assert buttons_list[0] not in chars_teams_list[9]
    assert buttons_list[1] in chars_teams_list[9]
    assert buttons_list[2] not in chars_teams_list[9]
    assert buttons_list[3] in chars_teams_list[9]

driver.close()
driver.quit()
