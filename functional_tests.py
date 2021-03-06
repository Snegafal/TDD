from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn("To-Do", self.browser.title)
        self.fail("test finished")

if __name__ == "__main__":
    unittest.main(warnings="ignore")