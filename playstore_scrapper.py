import csv

from selenium import webdriver

class PlaystoreScrapper():
    """
    Class to scrape app reviews along with star rating and date.
    """
    def __init__(self, url, app_name, no_of_pages=10):
        path_to_phantomjsdriver = r"C:\work\phantomjs-2.1.1-windows\bin\phantomjs.exe"
        self.browser = webdriver.PhantomJS(executable_path=path_to_phantomjsdriver)

        self.url = url
        self.app_name = app_name
        self.browser.get(url)

    def get_next_button():
        """
        Returns the next button element which takes the crawler
        to the next set of reviews.
        """
        next_button_xpath = r"//*[@id='body-content']/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button[2]/div[2]/div/div"
        return browser.find_element_by_xpath(next_button_xpath)


