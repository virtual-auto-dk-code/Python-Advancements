import selenium
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

print("program has started")
# Customary code starts
# driver_path = "/home/Projects/WebDrivers/Chrome_110.0.5481.77/chromedriver_linux64/chromedriver"
driver_path = ChromeDriverManager().install()
service = ChromeService(executable_path=driver_path)
chrome_options = ChromeOptions()
chrome_options.add_argument('--no-sandbox')  # Update
myDriver = webdriver.Chrome(service=service, options=chrome_options)
myDriver.set_page_load_timeout(60)
myDriver.maximize_window()
myDriver.implicitly_wait(30)
# Customary code ends

# opening website
myDriver.get("https://en.wikipedia.org/wiki/Computer")
#
# https://en.wikipedia.org/wiki/Animal

time.sleep(4)

actions = ActionChains(myDriver)
element = myDriver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[4]")
print(str(element.text))
element1 = myDriver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[5]")
print(str(element1.text))
actions.move_to_element(element)
actions.click_and_hold(on_element=element)
actions.release(on_element=element1)
actions.perform()

time.sleep(15)
print("Done")
myDriver.quit()
