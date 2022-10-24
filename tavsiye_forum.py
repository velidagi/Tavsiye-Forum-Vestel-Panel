import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
cevap = 1
browser = webdriver.Edge()
page_number = 0
messages_text = []
f = open("Mytext.txt", "w")
while page_number <= 854:

    page_number += 1
    browser.get("https://tavsiyeforumu.com/konu/vestel-panel-bilgi-hatti.449/page-"+str(page_number))
    messages = browser.find_elements(By.CLASS_NAME, "bbWrapper")

    for i in messages:
        try:
            f.write("Cevap-"+str(cevap)+i.text)
            f.write("\n-----------------------------------------------\n")
            cevap = +1
        except:
            pass





