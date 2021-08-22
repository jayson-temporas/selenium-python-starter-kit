import unittest
import config
from BaseTestCases import BaseTestCases

class HomePageTest(BaseTestCases.BaseTest):

    def test_homepage_loads_successfully(self):
        self.driver.get(config.path['host'])

        self.wait_for_page_load()

        self.assertIn('Google Search', self.driver.page_source)
    

if __name__ == "__main__":
    unittest.main()