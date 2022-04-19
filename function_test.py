from selenium import webdriver
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
        self.fail("Finish the test!")

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
    


#she types "Bye some peacock feathers" into a text box(Edith's hobby is trying fly-fishing lures) 

#when she hits enter, the page updates, and now the page lists 
#"1: Buy peacock feathers" as an item in a to-do list

#There is still a text box inviting her to add another item. She
#enters "Use peacock feathers to make a fly" (Edith us very methodical)

#the page updates again, and now shows both items on her list

#Edith wonder whether the site will remember her list. Then she sees
#that the site has generated a unique URL for her -- there is some 
#explanatory text to that effect

#she visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep 



