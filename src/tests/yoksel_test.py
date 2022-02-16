import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.utils.http import HttpUtils
from src.utils.url import UrlUtils
from pathlib import Path

script_dir = os.path.dirname(__file__)
driver_path = os.path.join(script_dir, '../drivers/chromedriver.exe')

results_path = os.path.join(script_dir, '../../results/')


class YokselTest:
    @staticmethod
    def run(urls):
        print('Yoksel test started')
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        print('Chrome driver run')
        driver.get('https://yoksel.github.io/html-tree/')
        print('Opened https://yoksel.github.io/html-tree/')
        time.sleep(2)

        count_errors = 0
        for url in urls:
            print('Start ' + url)
            project_document = HttpUtils.document(url)
            driver.execute_script('document.getElementsByTagName("textarea")[0].value = `' + str(project_document) + '`;')
            time.sleep(2)

            driver.find_element(By.TAG_NAME, 'textarea').send_keys(' ')
            time.sleep(2)

            driver.set_window_size(1920, 300)
            required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
            driver.set_window_size(1920, required_height)

            time.sleep(2)
            errors = driver.find_elements(By.CLASS_NAME, 'gnr-highlight-bem')



            saved_parents = []

            for error in errors:
                current = error
                for i in range(0, 7):
                    parent = current.find_element(By.XPATH, '..')
                    if parent:
                        current = parent
                    else:
                        break
                driver.execute_script('arguments[0].style.backgroundColor = "#f55"', current)

            if len(errors) > 0:
                project_name = UrlUtils.name(url)
                page_name = UrlUtils.page_name(url)
                Path(results_path + project_name).mkdir(parents=True, exist_ok=True)
                print('!!! HAS ERRORS !!! : ' + page_name)
                driver.find_element(By.CLASS_NAME, 'gnr-tree').screenshot(results_path + project_name + '/yoksel_' + page_name + '.png')

        driver.quit()
        if count_errors == 0:
            print('*** Yoksel success')
        else:
            print('*** Yoksel FAILURE - ' + str(count_errors))
