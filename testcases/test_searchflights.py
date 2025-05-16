import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack

@pytest.mark.usefixtures("init_driver")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()

    @data(("Singa", "Singapore, (SIN)", "To", "Tokyo, (NRT)", "(//div[@aria-label='Choose Friday, May 30th, 2025'])[1]", "2 Stop"), ("New", "New Delhi, (DEL)", "New", "New York, (JFK)", "(//div[@aria-label='Choose Saturday, May 31st, 2025'])[1]", "Non Stop"))
    @unpack
    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testyaml.yaml")
    # @data(*Utils.read_data_from_excel("C:\\python-selenium\\selenium-python-test-framework\\testdata\\testdataexcel.xlsx", "Sheet1"))
    # @unpack
    # @data(*Utils.read_data_from_csv("C:\\python-selenium\\selenium-python-test-framework\\testdata\\testdatacsv.csv"))
    # @unpack
    def test_search_flights_2_stops(self, depart_location, from_expected_city, going_to_location, to_expected_city, departure_date_xpath, stops):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()
        # Searching flights with from and to location with date.
        search_flight_result = self.lp.search_flights(depart_location, from_expected_city, going_to_location, to_expected_city, departure_date_xpath)

        # Scroll down the page to load all flight results.
        self.lp.page_scroll()

        # Apply the filter to show only flights with "1/2/Non Stop".
        search_flight_result.filter_flights_by_stop(stops)

        # Find all flight items that contain the text "1/2/Non Stop" after applying the filter.
        all_stops = search_flight_result.get_search_flight_results()

        # Count the number of "2 Stop" flights
        self.log.info(f'--> no of {stops} flights are: {len(all_stops)}')

        # Iterate through each flight item found with "1/2/Non Stop".
        self.ut.assert_list_item_text(all_stops, stops)
