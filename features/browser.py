from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def visit(self, url):
        self.driver.get(url)

    def find_by_id(self, selector):
        return self.driver.find_element_by_id(selector)

    def find_by_xpath(self, selector):
        return self.driver.find_element_by_xpath(selector)
