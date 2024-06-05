import selenium
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


print("program has started")
# Customary code starts
myDriver=selenium.webdriver.Chrome("D:\\Software\\ChromeDriver\\chromedriver.exe")
myDriver.set_page_load_timeout(60)
myDriver.maximize_window()
myDriver.implicitly_wait(30)
# Customary code ends

# opening website
myDriver.get("https://en.wikipedia.org/wiki/Animal")

time.sleep(4)

actions = ActionChains(myDriver)
element=myDriver.find_element_by_xpath("//*[@id='mw-content-text']/div/p[2]")
actions.move_to_element(element)
myDriver.switch_to_active_element()
time.sleep(5)
actions.move_by_offset(-(element.size["width"])/2, -(element.size["height"])/2)
actions.click()
ActionChains(myDriver).key_down(Keys.SHIFT)
actions.move_by_offset((element.size["width"]),(element.size["height"]))
actions.click()
#    actions.context_click()
actions.perform()

print("end of action")
print("Sucessfully came to the end")
#myDriver.quit()