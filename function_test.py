from email import header
import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        chrome_driver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
        self.browser =  webdriver.Chrome(executable_path = chrome_driver)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. 
        # She goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # she notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title), "Browser title was: " + self.browser.title
        
        #header_text = self.browser.find_element_by_tag_name('h1').text
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do',header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #she types "Bye some peacock feathers" into a text box(Edith's hobby is trying fly-fishing lures) 
        inputbox.send_keys('Buy peacock feathers')

        #when she hits enter, the page updates, and now the page lists 
        #"1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.Enter)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        #There is still a text box inviting her to add another item. She
        #enters "Use peacock feathers to make a fly" (Edith us very methodical)
        self.fail("Finish the test!")

        #the page updates again, and now shows both items on her list

        #Edith wonder whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some 
        #explanatory text to that effect

        #she visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep 


if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
    




