from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions() 
options.add_argument("window-size=1280,800")
options.add_argument('--disable-blink-features=AutomationControlled')
browser  = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(browser.execute_script("return navigator.userAgent;"))

# Open the Website
browser.get("https://www.walmart.com/")

# Put your information here
first_name = "" 
last_name = ""
address_line_one = ""
#address_line_two = ""
phone_number = ""
city = ""
email = ""
state = ""
zip_code = ""

#cc_number = ""
#cvv = ""


search_query = "knex"

search_bar = browser.find_element_by_id("global-search-input")
search_bar.send_keys(search_query)
sleep(.5)
search_bar.send_keys(Keys.ENTER)

sleep(.5)
browser.find_element_by_link_text("K'NEX Imagine - Creation Zone Building Set - 417 Pieces - Ages 5 and Up - Construction Educational Toy").click()

sleep(.5)
add_to_cart = browser.find_element_by_xpath('//span[text()="Add to cart"]')
add_to_cart.click()

sleep(1)
check_out = browser.find_element_by_xpath('//span[text()="Check out"]')
check_out.click()

sleep(2)
as_guest = browser.find_element_by_xpath('//span[text()="Continue without account"]')
as_guest.click()

sleep(1.5)
cont = browser.find_element_by_xpath('//span[text()="Continue"]')
cont.click()

sleep(1.5)
first_name_entry = browser.find_element_by_id("firstName")
sleep(.5)
first_name_entry.send_keys(first_name)

last_name_entry = browser.find_element_by_id("lastName")
sleep(.5)
last_name_entry.send_keys(last_name)

address_entry_line_one = browser.find_element_by_id("addressLineOne")
sleep(.5)
address_entry_line_one.send_keys(address_line_one)
address_entry_line_one.send_keys(Keys.ENTER)

#address_entry_line_two = browser.find_element_by_id("addressLineTwo")
#sleep(.5)
#address_entry_line_two.send_keys(address_entry_line_two)

email_entry = browser.find_element_by_id("email")
sleep(.5)
email_entry.send_keys(email)

state_entry = browser.find_element_by_id("state")
sleep(.5)
state_entry.send_keys(state)

postal_code = browser.find_element_by_id("city")
sleep(.25)
postal_code.send_keys(Keys.CONTROL + "a")
sleep(.25)
postal_code.send_keys(Keys.DELETE)
sleep(.25)
postal_code.send_keys(city)

postal_code = browser.find_element_by_id("postalCode")
sleep(.25)
postal_code.send_keys(Keys.CONTROL + "a")
sleep(.25)
postal_code.send_keys(Keys.DELETE)
sleep(.25)
postal_code.send_keys(zip_code)

state_entry = browser.find_element_by_id("phone")
sleep(.5)
state_entry.send_keys(phone_number)

# This is for hitting the continue button automatically, it's not really needed if you're not having the script
# input you CC number and CVV
#sleep(.5)
#cont = browser.find_element_by_xpath('//span[text()="Continue"]')
#cont.click() 
# When I updated the city, since it tries and detects based on browser location I had to hit this button twice 
# both when doing it manually and when running the script *shrug* so this may or may not be needed
#sleep(1)  
#cont.click()

#sleep(2)
#credit_card = browser.find_element_by_id("creditCard")
#sleep(.5)
#credit_card.send_keys(cc_number)

#cvv_entry = browser.find_element_by_id("cvv")
#sleep(.5)
#cvv_entry.send_keys(cvv)

# You could have the script handle inputing all of youy CC information if you want
# You'd have to expand it to work with dropdowns, which i think selenium you need to 
# do something like this.
#
# from selenium.webdriver.support.ui import Select # This should be at the top with your other imports
# 
# exp_month = ""
# exp_yr = ""
# month_entry = select = Select(driver.find_element_by_id('month-chooser'))
# month_entry.select_by_visible_text(exp_month)
# year_entry = select = Select(driver.find_element_by_id('year-chooser'))
# month_entry.select_by_visible_text(exp_yr)
# I haven't tested this code, but i think something along these lines should/would work.
