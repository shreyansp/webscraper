# import web driver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import logging
import config
import os

logging.basicConfig(format='%(asctime)s %(levelname)s[%(lineno)-3d]:%(message)s')
log = logging.getLogger(__name__)
log.setLevel(level=logging.DEBUG)

class BaseScraper():
    def __init__(self):
        self.driver = webdriver.Chrome(config.CHROME_DRIVER)
        self.driver.implicitly_wait(3)
        log.info("BaseScraper __init__ done")

    def _get_element_text(self, selector=None, element=None, parent=None):
        try:
            if element:
                elem = element
            else:
                if not parent:
                    parent = self.driver
                elem = parent.find_element_by_css_selector(selector)
            return elem.text
        except NoSuchElementException:
            return None

    def ajax_wait(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
                    self.ajax_complete,  "Timeout waiting for page to load")

    @staticmethod
    def ajax_complete(driver):
        try:
            return 0 == driver.execute_script("return jQuery.active")
        except WebDriverException:
            pass
