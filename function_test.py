from selenium import webdriver

chrome_driver=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
brower = webdriver.Chrome(executable_path=chrome_driver)
brower.get('http://localhost:8000')

assert "The install worked successfully! Congratulations!" in brower.title