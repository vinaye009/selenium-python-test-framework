import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class SearchFlightResults(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ------------------ Locators ------------------
    FILTER_BY_ONE_STOP_ICON = "//p[contains(@class,'font-lightgrey bold')][normalize-space()='1']"
    FILTER_BY_TWO_STOP_ICON = "//p[contains(@class,'font-lightgrey bold')][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[contains(@class,'font-lightgrey bold')][normalize-space()='0']"

    SEARCH_FLIGHT_RESULTS_XPATH = "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]"

    # ------------------ Actions ------------------
    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_ONE_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_TWO_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.warning("--> Selected flights with 1 Stop.")
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            self.log.warning("--> Selected flights with 2 Stops.")
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            self.log.warning("--> Selected flights with Non Stop.")
        else:
            self.log.warning("--> Provide a valid filter option")

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS_XPATH)



