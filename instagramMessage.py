from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pwinput
from selenium.webdriver.support.wait import WebDriverWait


kullaniciAdi = input("kullanıcı adını gir: ")
sifre = pwinput.pwinput(prompt='Şifre: ')
mesajKisi = input("Mesaj göndermek istediğiniz kişinin kullanıcı adı: ")
mesaj = input("Mesajınız: ")

chrome_driver_path = "C:\drivers\chromedriver"

driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(10)

url = "https://www.instagram.com/"


driver.get(url)


username = driver.find_element(By.NAME,"username")
username.send_keys(kullaniciAdi)

password = driver.find_element(By.NAME,"password")
password.send_keys(sifre)
password.send_keys(Keys.ENTER)


notnow = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div/div/button')
notnow.click()


notnow1 = driver.find_element(By.XPATH,'/html/body')
notnow1.click()


notnow2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
notnow2.click()


message = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div[3]/div/a/div')
message.click()


selection = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button')
selection.click()


who = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')
who.send_keys(mesajKisi)


choise = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button')
choise.click()


go = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button')
go.click()

write = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
write.send_keys(mesaj)
write.send_keys(Keys.ENTER)

