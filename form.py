from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from time import time, sleep
from selenium.webdriver.chrome.options import Options
from random import choice
import smtplib as sm
from properties import *

# ======================= constants ====================== #
form_url = 'https://forms.gle/weSgq5z5RYyTsp4V6'

chrome_driver = "G:/My Drive/Programming/z - tools/chromedriver.exe"

smtp, gmail, pwd = 'smtp.gmail.com', 'elder.estuda.voce.recebe.email@gmail.com', 'e4r5t6y7'

# =================== keep window open =================== #
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# ======================= functions ======================= #
class Form:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver))

    def run(self, entries):
        self.driver.get(url=form_url)
        for n in range(0, len(entries)):
            n = entries[n]
            sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(n['address'])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(n['price'].split('+')[0])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(n['link'])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
            sleep(1)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
        self.driver.quit()

    def send(self):
        msg = self.frase_de_hoje
        with sm.SMTP(smtp, port=587) as mail:
            mail.starttls()
            mail.login(user=gmail, password=pwd)
            mail.sendmail(from_addr=gmail, to_addrs=email, msg=f'Subject: Desmotive-se!\n\n{msg}')
            print(msg)



