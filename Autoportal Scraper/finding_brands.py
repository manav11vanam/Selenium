from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse
from finding_models import model

def find_model(driver, url):
    driver.get(url)
    driver.find_element_by_class_name('btn-more-plus').click()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    uls = soup.find_all('ul', class_='car-type-list car-type-brand row-flex')
    brands = []
    for ul in uls:
        a_tags = ul.find_all('a')
        tmp = [urllib.parse.urljoin(url, a_tag.get('href')) for a_tag in a_tags]
        brands.extend(tmp)
    print(len(brands))
    # print(brands)
    for brand in brands[6:]:
        model(driver, brand)

if __name__ == '__main__':
    url = 'https://autoportal.com/newcars/'
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(PATH, options=options)
    find_model(driver, url)
    driver.quit()
