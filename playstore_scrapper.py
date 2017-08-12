import csv

from selenium import webdriver


class PlaystoreScrapper():
    """
    Class to scrape app reviews along with the star rating and date.
    """
    def __init__(self, url, app_name, no_of_pages=10):
        path_to_phantomjsdriver = r"C:\work\phantomjs-2.1.1-windows\bin\phantomjs.exe"
        self.browser = webdriver.PhantomJS(executable_path=path_to_phantomjsdriver)

        self.url = url
        self.app_name = app_name
        self.no_of_pages = no_of_pages

    def get_next_button(self):
        """
        Returns the next button element which takes the crawler
        to the next set of reviews.
        """
        next_button_xpath = r"//*[@id='body-content']/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button[2]/div[2]/div/div"
        return self.browser.find_element_by_xpath(next_button_xpath)

    def filter_reviews(self, reviews):
        """
        Some captured review elements do not have app reviews.
        This filters such reviews.
        """
        return [review for review in reviews if review.text]

    def get_reviews_data(self, reviews):
        page_reviews = []
        for review in reviews:
            review_date = review.find_element_by_css_selector(".review-date")
            star_rating = review.find_element_by_css_selector(".star-rating-non-editable-container").get_attribute("aria-label")
            review_text = review.find_element_by_css_selector(".with-review-wrapper")

            review_data = [review_date.text, star_rating, review_text.text]
            page_reviews.append(x.encode("utf-8") for x in review_data)
        return page_reviews

    def to_csv(self):

        self.browser.get(self.url)
        with open("{app_name}_reviews.csv".format(app_name=self.app_name), "w+") as file:
            writer = csv.writer(file)
            column_headers = ["Date", "Rating", "Text"]
            writer.writerows([column_headers])

            next_button = self.get_next_button()

            for i in range(self.no_of_pages):
                next_button.click()
                reviews = self.browser.find_elements_by_css_selector(".single-review")
                reviews_data = self.get_reviews_data(self.filter_reviews(reviews))
                for data in reviews_data:
                    writer.writerows(data)
