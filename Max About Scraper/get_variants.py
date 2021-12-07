from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

PATH = 'C:\Program Files (x86)\chromedriver.exe'
def get_links_variants(url):
    driver = webdriver.Chrome(PATH)
    driver.get(url)

    driver.find_element_by_css_selector('#VehicleInfoTabs > li:nth-child(2) > a').click()

    soup = BeautifulSoup(driver.page_source, 'lxml')
    vars = soup.find('ul', class_='variants')
    variants = [a.get('href') for a in vars.find_all('a')]
    driver.quit()
    s = "\n".join(variants) + '\n'
    with open('links.txt', 'a') as f:
        f.write(s)

if __name__ == "__main__":
    url = 'https://autos.maxabout.com/cars/hyundai/santro/santro-new'
    get_links_variants(url)
