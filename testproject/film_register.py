import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

url = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"
driver.get(url)
time.sleep(2)

# TC1: check that 24 pcs of films has been displayed on the screen

films = driver.find_elements_by_xpath('//h2')
time.sleep(2)

assert (len(films)) == 24
time.sleep(2)

# TC2: new film registration

reg_btn = driver.find_element_by_class_name("mostra-container-cadastro")
save_btn = driver.find_element_by_xpath('//button[@onclick="salvarFilme()"]')

title = driver.find_element_by_id("nomeFilme")
rel_year = driver.find_element_by_id("anoLancamentoFilme")
chron_year = driver.find_element_by_id("anoCronologiaFilme")
trailer = driver.find_element_by_id("linkTrailerFilme")
image = driver.find_element_by_id("linkImagemFilme")
summary = driver.find_element_by_id("linkImdbFilme")


def new_reg(new_film):
    reg_btn.click()
    time.sleep(2)
    title.send_keys(new_film[0])
    rel_year.send_keys(new_film[1])
    chron_year.send_keys(new_film[2])
    trailer.send_keys(new_film[3])
    image.send_keys(new_film[4])
    summary.send_keys(new_film[5])
    save_btn.click()


# test data for registration
my_new_film = [
    "Black widow",
    "2021",
    "2020",
    "https://www.youtube.com/watch?v=Fp9pNPdNwjI",
    "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg",
    "https://www.imdb.com/title/tt3480822/"
]

new_reg(my_new_film)
time.sleep(2)

# check that 25 pcs of films has been displayed on the screen
films = driver.find_elements_by_xpath('//h2')
time.sleep(2)
assert (len(films)) == 25

driver.close()
driver.quit()
