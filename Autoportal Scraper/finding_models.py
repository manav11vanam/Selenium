import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse
from model_variants import combined_function

def model(driver, url):
    # res = requests.get(url)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    section = soup.find('section', class_='m_b-20')
    a_tags = section.find_all('a', class_='model-list__title')
    models = []
    for a_tag in a_tags:
        models.append(urllib.parse.urljoin(url, a_tag.get('href')))
    for model in models:
        combined_function(model)

if __name__ == '__main__':
    url = 'https://autoportal.com/newcars/marutisuzuki/'
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(PATH, chrome_options=options)
    model(driver, url)
