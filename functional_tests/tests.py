from email import header
import imp
from re import M
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import unittest
MAX_WAIT = 10
chrome_driver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser =  webdriver.Chrome(executable_path = chrome_driver)
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return 
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time < MAX_WAIT:
                    raise e
                time.sleep(0.5)
    
    def test_multiple_users_can_start_lists_at_differents_urls(self):
        #Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        #Now use a new browser session to make sure that no imformation
        ## of Edith's  is comming through  from cookies etc
        self.browser.quit()
        self.browser = webdriver.Chrome(executable_path = chrome_driver)

        #Francis visits the home page. There is no sign of Edith's
        #list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        #Francis start a new list by entering a new. He
        #is less interesting than Edit
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        #Francis gets his own uqniu URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #Again there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        #satisfy

            

    def test_can_start_a_list_for_one_user(self):
        # Edith has heard about a cool new online to-do app. 
        # She goes to check out its homepage.
        
        #self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)

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
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #There is still a text box inviting her to add another item. She
        #enters "Use peacock feathers to make a fly" (Edith us very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feather to make a fly')
        inputbox.send_keys(Keys.ENTER)
    
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feather to make a fly')



        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     f"New to do item did not appear in table. Contents were:\n{table.text}"
        # )


    

        #the page updates again, and now shows both items on her list

        #Edith wonder whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some 
        #explanatory text to that effect

        #she visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep 
    




