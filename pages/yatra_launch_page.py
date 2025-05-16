import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.search_flights_results_page import SearchFlightResults
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ------------------ Locators ------------------
    DEPART_FROM_FIELD_XPATH = "(//div[@role='Combobox']//p[@title])[1]"
    DEPART_FROM_INPUT_ID = "input-with-icon-adornment"
    DEPART_FROM_RESULTS_XPATH = "//div[contains(@class,'MuiBox-root')]//ul[1]/div"

    GOING_TO_FIELD_XPATH = "//p[text()='Going To']"
    GOING_TO_INPUT_ID = "input-with-icon-adornment"
    GOING_TO_RESULTS_XPATH = "//div[contains(@class,'MuiBox-root')]/ul[1]/div"

    BACKDROP_CLASS_NAME = "MuiBackdrop-root"

    DATE_PICKER_XPATH = "//div[@class='css-w7k25o']"

    SEARCH_BUTTON_XPATH = "//button[text()='Search']"

    # ------------------ Actions ------------------
    def going_from(self, depart_location, from_expected_city):
        # Click on the departure from field
        departure_field = self.wait_for_presence_of_all_elements(By.XPATH, self.DEPART_FROM_FIELD_XPATH)
        if departure_field:
            departure_field[0].click()

        # Enter the departure location
        self.visibility_of_element_located(By.ID, self.DEPART_FROM_INPUT_ID).send_keys(depart_location)
        time.sleep(0.5)

        # Look for auto-suggested departure locations
        search_results = self.wait_for_presence_of_all_elements(By.XPATH, self.DEPART_FROM_RESULTS_XPATH)

        # Select the expected departure city from the results
        for result in search_results:
            if from_expected_city in result.text:
                result.click()
                break

    def going_to(self, going_to_location, to_expected_city):
        # Click "Going To" field
        self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD_XPATH).click()
        self.log.info("--> Clicked on going to field successfully.")

        # Enter destination location
        self.visibility_of_element_located(By.ID, self.GOING_TO_INPUT_ID).send_keys(going_to_location)
        self.log.info("--> Typed text into going to field successfully.")
        time.sleep(0.5)

        # Get search results for destination city
        go_results = self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULTS_XPATH)

        # Select the expected destination city from the results
        for result in go_results:
            if to_expected_city in result.text:
                result.click()
                break


    def wait_for_backdrop_to_disappear(self):
        # Wait until the backdrop disappears
        self.invisibility_of_element_located(By.CLASS_NAME, self.BACKDROP_CLASS_NAME)

    def select_date(self, departure_date_xpath):
        # Click the date picker field
        self.wait_until_element_is_clickable(By.XPATH, self.DATE_PICKER_XPATH).click()

        # Select the specified departure date
        self.wait_until_element_is_clickable(By.XPATH, departure_date_xpath).click()

    def click_search(self):
        # Click the "Search" button
        self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_BUTTON_XPATH).click()
        time.sleep(1)


    def search_flights(self, depart_location, from_expected_city, going_to_location, to_expected_city, departure_date_xpath):
        # Performs a complete flight search operation.
        self.going_from(depart_location, from_expected_city)
        self.going_to(going_to_location, to_expected_city)
        self.wait_for_backdrop_to_disappear()
        self.select_date(departure_date_xpath)
        self.click_search()

        # Initialize the SearchFlightResults page object and return it.
        search_flight_result = SearchFlightResults(self.driver)
        return search_flight_result


