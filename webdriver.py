from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdrivermanager import ChromeDriverManager
import os


class Webdriver():
    page_load_timeout = 60
    wait_timeout = 10
    headless = False
    profile = False
    driver = object
    wait = object

    def set_headless(self,headless):
        self.headless=headless

    def set_wait_timeout(self,wait_timeout=10):
        self.wait_timeout=wait_timeout

    def set_page_load_timeout(self,page_load_timeout=60):
        self.page_load_timeout=page_load_timeout

    def set_driver(self,driver):
        self.driver=driver

    def set_wait(self,wait):
        self.wait=wait

    def update(self, path):
        gdd = ChromeDriverManager(link_path=path)
        version=gdd.get_compatible_version()
        path=gdd.download_and_install(version)
        return path[1]._str

    def start(self):
        home = os.path.expanduser('~')
        self.path_dow = os.path.join(home, 'Downloads')
        options = webdriver.ChromeOptions()

        if self.profile:
            dir_path = os.getcwd()
            profile = os.path.join(dir_path, "profile", "wpp")        
            self.options.add_argument(r"--user-data-dir={}".format(profile))

        if self.headless:
            options.headless = self.headless
            options.add_argument('--blink-settings=imagesEnabled=false')

        options.add_argument("--safebrowsing-disable-download-protection")
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument('--disable-extensions')
        options.add_argument('--kiosk-printing')
        options.add_argument('--no-proxy-server')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--log-level=3')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--safebrowsing-disable-extension-blacklist')

        config_print = '''{"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}], 
                    "selectedDestinationId": "Save as PDF",
                    "version": 2}'''

        prefs = {'download.download_directory': True,
                 "download.default_directory": self.path_dow,
                 'donwload.prompt_for_download': False,
                 "download.directory_upgrade": True,
                 'plugins.always_open_pdf_externally': True,
                 'download.extensions_to_open': 'xml',
                 'profile.default_content_setting_values.automatic_downloads': 1,
                 'safebrowsing.enabled': 'false',
                 }

        options.add_experimental_option('prefs', prefs)

        chromedriver_path = "binaries"

        try:
            self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        except:
            self.driver = webdriver.Chrome(self.update(chromedriver_path), options=options)

        self.driver.set_page_load_timeout(self.page_load_timeout)
        self.wait = WebDriverWait(self.driver, self.wait_timeout)
        self.driver.maximize_window()

    def finish(self):
        try:
            self.driver.quit()
            self.driver = None
        except:
            pass

    def restart(self):
        self.finish()
        self.start()

# web = Webdriver()
# web.start()
# driver = web.driver
# driver.get('https://pt.stackoverflow.com/questions/328572/janela-de-imprimir-salvar-pdf-selenium-webdriver')
# driver