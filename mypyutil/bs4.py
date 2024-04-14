import random
import time
import requests
from requests_cache import CachedSession
from bs4 import BeautifulSoup

from selenium import webdriver

def selenium_get(url, fpath_cache, func_check_valid, func_handle=None, flg_waiting=True):
    if not os.path.exists(fpath_cache):
        if selenium_get.driver is None:
            selenium_get.driver = webdriver.Chrome()
        print("selenium_get actual work") # debug
        selenium_get.driver.get(url)
        if func_handle is not None:
            func_handle(selenium_get.driver)
        soup = BeautifulSoup(selenium_get.driver.page_source, "html.parser")
        if not func_check_valid(soup) and flg_waiting:
            input("waiting any")
        pickle.dump(soup, open(fpath_cache, "wb"))
        time.sleep(1 + 3 * random.random() * 2)
    else:
        print('selenium_get cache') # debug
    obj = pickle.load(open(fpath_cache, "rb"))
    return obj
selenium_get.driver = None

def scroll_page(driver): # you can use as func_handle
    prev_height = -1
    max_scrolls = 100
    scroll_count = 0
    time.sleep(2)
    while scroll_count < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # give some time for new results to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height
        scroll_count += 1

url = "https://requests-cache.readthedocs.io/en/stable/user_guide/general.html"
def cheetsheet(url):

    # session
    session = CachedSession()
    print('session.cache.db_path') # debug
    pp(session.cache.db_path) # debug
    headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            }
    response = session.get(url, headers=headers)
    print('response.from_cache', response.from_cache) # debug
    print('response.created_at', response.created_at) # debug
    print('response.expires', response.expires) # debug

    # soup
    soup = BeautifulSoup(response.content, "html.parser")
    tag_title = soup.find(class_="sg-corporate-name")
    tag_body = soup.find("article", class_="pg-body")
    url = soup.find("a").get("href")
    text = tag_title.text + "\n" + tag_body.text
    return tag_title.text, text
    open("soup.html", "w", encoding="utf_8_sig").write(soup.prettify())

    # sleep
    session = CachedSession()
    upto = 19
    for page in range(1, upto + 1):
        url = f"https://hoge.com?page={page}"
        response = session.get(url)
        if not response.from_cache:
            time.sleep(1 + 3 * random.random() * 2)

    # raw
    requests.get(url)

