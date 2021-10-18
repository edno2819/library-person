from selenium.webdriver.remote.remote_connection import LOGGER, logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver import Webdriver as Webdriver_base
import pandas as pd 
import time
import os


LOGGER.setLevel(logging.WARNING)


class Webdriver():
    def __init__(self, headless=False, profile=False):
        self.webdriver = Webdriver_base()
        self.webdriver.profile = profile
        self.webdriver.headless = headless

    def start(self):
        self.webdriver.start()
        self.driver = self.webdriver.driver
        self.wait = self.webdriver.wait

    def open_page(self,url):
        self.driver.get(url)
    
    def find_element(self, locator, elem=None):
        by, locator = locator
        if elem:
            return elem.find_element(by, locator)
        else:
            return self.driver.find_element(by, locator)

    def find_elements(self, locator, elem=None):
        by, locator = locator
        if elem:
            return elem.find_elements(by, locator)
        else:
            return self.driver.find_elements(by, locator)

    def move_element(self, elem, y=-100):
        if type(elem)==tuple:
            elem = self.find_element(elem)

        loc=elem.location_once_scrolled_into_view
        self.driver.execute_script(f"window.scrollBy({loc['x']},{y})")

    def click(self, locator, hover_to=True):
        elem = locator
        if type(locator) is tuple:
            elem = EC.element_to_be_clickable(locator)
            elem = self.wait.until(elem)
        if hover_to:
            self.move_element(elem)
        elem.click()
        
    def exist(self,element, wait=10, retur=False):
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located(element)
                    )
            if retur: return element
            return True
        except:
            return False

    def fill(self, element, text):
        if type(element)==tuple:
            elem = EC.element_to_be_clickable(element)
            elem = self.wait.until(elem)

        self.move_element(elem)
        elem.click()
        elem.clear()
        elem.send_keys(text)

    def get_element_attribute(self, locator, attribute):
        elem = locator
        if type(locator) is tuple:
            elem = EC.presence_of_element_located(locator)
            elem = self.wait.until(elem)
        attribute = elem.get_attribute(attribute)
        return attribute

    def send_key(self, key, element=None):
        if element:
            return self.driver.find_element(element[0],element[1]).send_keys(key)
        else:
            return ActionChains(self.driver).send_keys(key).perform()

    def refresh(self):
        self.driver.refresh()

    def switch_to_frame(self, frame="son_frame"):
        if frame == 'root_frame':
            self.driver.switch_to.default_content()
        else:
            self.driver.switch_to.frame(frame)

    def wait_download(self):
        file = os.listdir(self.webdriver.downloads_path)[0]
        if '.tmp' not in file:
            if '.crdownload' not in file:
                time.sleep(1)
                return file

    def zoom(self,zoom):
        self.driver.execute_script(f"document.body.style.zoom='{zoom}'")

    def screenshot(self, file, zoom='100%', add_timestamp=False):
        self.zoom(zoom)
        self.driver.save_screenshot(f'{file}.png') if not add_timestamp else self.driver.save_screenshot(f'{file} {time.time()}.png')
        self.zoom('100%')

    def get_table(self, elem, header=0):
        return pd.read_html(elem.get_attribute('outerHTML'), header=header)[0]
    
    def full_screenshot(self, path) -> None:
        original_size = self.driver.get_window_size()
        required_width = self.driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')
        self.driver.set_window_size(required_width, required_height)
        self.driver.save_screenshot(path)  # has scrollbar
        self.driver.find_element_by_tag_name('body').screenshot(path)  # avoids scrollbar
        self.driver.set_window_size(original_size['width'], original_size['height'])

    def close(self):
        self.driver.quit()

    def save_as_pdf(self, name_file, path_new):
        home = os.path.expanduser('~')
        path = os.path.join(home, 'Downloads')

        self.driver.execute_script('window.print();')
        file = self.wait_download()
        try:
            os.rename(f'{path}\\{file}',f'{path_new}\\{name_file}.pdf')
        except:
            pass

    def wait_download(self):
        home = os.path.expanduser('~')
        path = os.path.join(home, 'Downloads')
        file = os.listdir(path)[0]
        if '.tmp' not in file:
            if '.crdownload' not in file:
                time.sleep(1)
                return file
        