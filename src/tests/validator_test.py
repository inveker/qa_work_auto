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


class ValidatorTest:
    @staticmethod
    def run(urls):
        print('Validator test started')
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        print('Chrome driver run')
        driver.get('https://validator.w3.org/nu/')
        print('Opened https://validator.w3.org/nu/')
        time.sleep(2)
        select = Select(driver.find_element(By.ID, 'docselect'))
        select.select_by_visible_text('text input')
        time.sleep(1)

        count_errors = 0
        for url in urls:
            print('Start ' + url)
            project_document = HttpUtils.document(url)
            driver.execute_script('document.getElementById("doc").value = `' + str(project_document) + '`;')
            time.sleep(1)
            driver.find_element(By.ID, 'submit').click()
            time.sleep(2)

            driver.set_window_size(1920, 300)
            required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
            driver.set_window_size(1920, required_height)

            error = driver.find_elements(By.CLASS_NAME, 'error')
            if len(error) > 0:
                count_errors += 1
                project_name = UrlUtils.name(url)
                page_name = UrlUtils.page_name(url)
                print('!!! HAS ERRORS !!! : ' + page_name)
                Path(results_path + project_name).mkdir(parents=True, exist_ok=True)
                driver.find_element(By.CSS_SELECTOR, '#results > ol').screenshot(
                    results_path + project_name + '/validator_' + page_name + '.png')
                time.sleep(1)

        driver.quit()
        if count_errors == 0:
            print('*** Validator success')
        else:
            print('*** Validator FAILURE - ' + str(count_errors))
