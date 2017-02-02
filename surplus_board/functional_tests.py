import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/yurychu/programs/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_adding_a_list_items_and_retireve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Surplus Board', self.browser.title)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

print('Hello!')
