import time
import re

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.maximize_window()
    return driver


def get_links():
    links = []
    for i in range(1, 171):
        url = 'https://planeta.ru/search/projects?category=CHARITY&status=SUCCESSFUL&page=' + str(i)
        links.append(url)
    print(links, len(links))
    return links


def dump_links_to_file(driver):
    with open("planeta_full.txt", 'w') as myfile:
        for page in get_links():
            #print(page)
            driver.get(page)
            time.sleep(10)
            content = driver.page_source
            myfile.write(content)


def get_project_links():
    project_urls = []
    with open("planeta_full.txt", 'r') as myfile:
        myfile = myfile.read()
        result = re.findall(r'\/campaigns\/.[^\"]+', myfile)
        for uniquelink in result:
            project_urls.append("https://planeta.ru" + uniquelink)
        #print(project_urls)
        print(len(project_urls))
    return project_urls


def get_xpath_text_or_nan(wait, xpath):
    try:
        x = wait.until(EC.presence_of_element_located((By.XPATH, xpath))).text
    except Exception as e:
        print("Got exception {}".format(repr(e)))
        x = ""
    return x


def get_title(wait):
    return get_xpath_text_or_nan(wait, '//h1[@class="project-view_name ng-star-inserted"]')


def get_briefly(wait):
    return get_xpath_text_or_nan(wait, '//p[@class="project-view_short-desc ng-star-inserted"]')


def get_description(wait):
    return get_xpath_text_or_nan(wait, '//div[@class="project-description sub-content ng-star-inserted"]')


def get_result(wait):
    return get_xpath_text_or_nan(wait, '//div[@class="project-view-meta_amount-val ng-star-inserted"]')


def get_goal(wait):
    return get_xpath_text_or_nan(wait, '//span[@class="project-view-meta_amount-lbl-val"]')


def get_donations(wait):
    return get_xpath_text_or_nan(wait, '//div[@class="project-view-info_lbl"][text() ="Поддержали"]/preceding-sibling::*')


def get_start(wait):
    return get_xpath_text_or_nan(wait, '//div[@class="project-view-info_lbl"][text() ="Запущен"]/preceding-sibling::*')


def get_finish(wait):
    return get_xpath_text_or_nan(wait, '//div[@class="project-view-info_lbl"][text() ="Завершен"]/preceding-sibling::*')

def get_author(wait):
    return get_xpath_text_or_nan(wait, '//div[@class="project-author_name project-author_name__info"]')


def extract_page(driver, url, data_frame):
    print(url)
    driver.get(url)
    time.sleep(4)
    wait = WebDriverWait(driver, 10)

    title = get_title(wait)
    author = get_author(wait)
    goal = get_goal(wait)
    donations = get_donations(wait)
    briefly = get_briefly(wait)
    description = get_description(wait)
    result = get_result(wait)
    start = get_start(wait)
    finish = get_finish(wait)

    data_frame["Title"].append(title)
    data_frame["Author"].append(author)
    data_frame["Briefly"].append(briefly)
    data_frame["Description"].append(description)
    data_frame["Goal"].append(goal)
    data_frame["Result"].append(result)
    data_frame["Donations"].append(donations)
    data_frame["Start"].append(start)
    data_frame["Finish"].append(finish)

    return data_frame

def get_data_frame():
    data_frame = {
    "Title": [],
    "Author": [],
    "Briefly": [],
    "Description": [],
    "Goal": [],
    "Result": [],
    "Donations": [],
    "Start": [],
    "Finish": []
    }
    return data_frame


if __name__ == "__main__":
    driver = get_driver()
    driver.get("http://planeta.ru")
    dump_links_to_file(driver)

    data_frame = get_data_frame()

    for url in get_project_links():
        data_frame = extract_page(driver, url, data_frame)

    PLdataset = pd.DataFrame(data_frame)
    PLdataset.to_csv('PLdataset.csv')
