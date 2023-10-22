import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import smtplib #email stuff

def SendEmail(recipiant, message, subject):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("YOUR_BOT_EMAIL_HERE@GMAIL.COM", "YOUR_BOT_PASSWORD")
    # attach subject to message
    RefinedMessage = "Subject: {}\n\n{}".format(subject,message)
    s.sendmail("YOURBOTEMAILHERE@GMAIL.COM", str(recipiant), RefinedMessage)
    # terminating the session
    s.quit()


InStockList = []

print("starting selenium...")
chrome_options = Options()
chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--enable-crash-reporter")
chrome_options.add_argument("--headless")
#chrome_options.add_argument('--ignore-certificate-errors')
#chrome_options.add_argument('--allow-running-insecure-content')
driver = webdriver.Chrome(options=chrome_options)

driver.set_window_size(1024, 768)

driver.get('https://vilros.com/products/raspberry-pi-zero-2-w?src=raspberrypi')
#/html/body/main/div[1]/div/div[1]/div[1]/div/div[2]/div/form/div[1]/div[2]/button/span [Full XPATH as of July 22]
search = driver.find_element(By.XPATH, "//div[2]/button/span").get_attribute("innerHTML")
if search.replace(" ","").replace("\n","") != "SoldOut":
    print("Vilros in stock!")
    InStockList.append("https://vilros.com/products/raspberry-pi-zero-2-w?src=raspberrypi")

driver.get('https://chicagodist.com/products/raspberry-pi-zero-2?src=raspberrypi')
search = driver.find_element(By.CLASS_NAME, "sold_out").get_attribute("innerHTML")
if search.replace(" ","").replace("\n","") != "SoldOut":
    print("Chicagodist in stock!")
    InStockList.append("https://chicagodist.com/products/raspberry-pi-zero-2?src=raspberrypi")

driver.get('https://www.pishop.us/product/raspberry-pi-zero-2-w/?src=raspberrypi')
search = driver.find_element(By.ID, "form-action-addToCart").get_attribute("value")
if search.replace(" ","").replace("\n", "") != "Outofstock":
    print("Pishop in stock!")
    InStockList.append("https://www.pishop.us/product/raspberry-pi-zero-2-w/?src=raspberrypi")

driver.get('https://www.canakit.com/raspberry-pi-zero-2-w.html?cid=usd&src=raspberrypi')
try:
    search = driver.find_element(By.XPATH, "//tr[1]/td[3]/div/a/span").get_attribute("innerHTML")
except:
    search = "InStock"
if search == "InStock":
    print("Canakit in stock!")
    InStockList.append("https://www.canakit.com/raspberry-pi-zero-2-w.html?cid=usd&src=raspberrypi")

driver.get("https://www.adafruit.com/piz2w?src=raspberrypi")
search = driver.find_element(By.XPATH, '//*[@itemprop="availability"]').get_attribute("innerHTML")
if search.replace(" ","").replace("\n", "") != "Outofstock":
    print("Adafruit in stock!")
    InStockList.append("https://www.adafruit.com/piz2w?src=raspberrypi")


if (len(InStockList) > 0):
    SendEmail("WHO_YOU_WANT_TO_RECIEVE_NOTIFICATIONS@GMAIL.COM", "Look here for the goods: " + "\n".join(InStockList), "RaspPi 2W In Stock!")
else:
    print("No stock found :(")
exit()
