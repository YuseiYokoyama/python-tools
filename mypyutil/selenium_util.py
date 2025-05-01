from selenium import webdriver

def set_checkbox(e_checkbox, flg):
    if e_checkbox.is_selected() != flg:
        e_checkbox.click()

from pprint import pprint as pp
from pprint import pformat as pf

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class BrowserController():

    def __init__(self, dirpath_save):
        self.basic_implicitly_wait = 10
        self.driver = self.make_driver(self.basic_implicitly_wait)
        self.dirpath_save = dirpath_save
        os.makedirs(self.dirpath_save, exist_ok=True)


    def make_driver(self, basic_implicitly_wait):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('detach', True) # if False then remain open
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(basic_implicitly_wait)
        return driver

    def access(self, page=None):
        if page is None:
            url = "https://salesnow.jp/db/industries/entertainment/subIndustries/hotel-staying"
        else:
            url = f"https://salesnow.jp/db/industries/entertainment/subIndustries/hotel-staying/page/{page}"
        self.driver.get(url)
        selector = "#__BVID__13"
        input_user_id = self.driver.find_element(By.CSS_SELECTOR, selector)
        input_user_id.send_keys(user_id)
        selector = "#__BVID__16"
        input_password = self.driver.find_element(By.CSS_SELECTOR, selector)
        input_password.send_keys(password)

    def go_next_page(self):
        selector = "#__next > div.Layout_container__hieOS > div.Layout_contentContainer__7mnrB > main > div.SearchResult_container__Mn1_C > div.Pagination_container__tEfKA > a"
        link_list = self.driver.find_elements(By.CSS_SELECTOR, selector)
        print('link_list') # debug
        pp(link_list) # debug
        link_next_page = link_list[-1]
        link_next_page.click()
        self.save_list_page()

    def save(self, name):
        if not self.check_health():
            raise RuntimeError
        fpath = os.path.join(self.dirpath_save, name + ".html")
        open(fpath, "w").write(self.driver.page_source)
        print('saved', name) # debug

