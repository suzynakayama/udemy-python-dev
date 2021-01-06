from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')      # because we downloaded, copied and pasted in this folder

# # If run the line below, it will open a new chrome window/instance
# print(chrome_browser)

chrome_browser.maximize_window() # to open the new window maximized

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title         # assert is not used a lot because it will error out if it is False

btn = chrome_browser.find_element_by_class_name('btn-default')

# print(btn)            prints the selenium webelement

btn_text = btn.get_attribute('innerHTML')

# print(btn_text)

assert 'Show Message' in chrome_browser.page_source     # check if is in the html source of the page

## Close the ads
lightbox_close_x = chrome_browser.find_element_by_id("at-cv-lightbox-close")
lightbox_close_x.click()

ipt = chrome_browser.find_element_by_id('user-message')     # get the input
ipt.clear()     # clear the input
ipt.send_keys('I am super cool!')       # write in the input

btn.click()

output_msg = chrome_browser.find_element_by_id('display')

assert 'I am super cool!' in output_msg.text

all_btns = chrome_browser.find_element_by_css_selector('.btn')

# print(all_btns)

chrome_browser.close()      # sometimes there are bugs with this, so sometimes you need to call this twice

# chrome_browser.quit()     # it will quit the browser/session

#! WAITS --> you can use time.sleep() to vai for some time before running the next of the code to simulate it is a human and not being caught by the websites as a robot