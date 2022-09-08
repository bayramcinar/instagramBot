from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pwinput



kullaniciAdi = input("kullanıcı adını gir: ")
sifre = pwinput.pwinput(prompt='Şifre: ')
mesajKisi = input("Mesaj göndermek istediğiniz kişinin kullanıcı adı: ")
mesaj = input("Mesajınız: ")

chrome_driver_path = "C:\drivers\chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

url = "https://www.instagram.com/"


driver.get(url)

time.sleep(3)

username = driver.find_element(By.NAME,"username")
username.send_keys(kullaniciAdi)

password = driver.find_element(By.NAME,"password")
password.send_keys(sifre)
password.send_keys(Keys.ENTER)

time.sleep(5)

notnow = driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')
notnow.click()

time.sleep(2)

notnow1 = driver.find_element(By.XPATH,'/html/body')
notnow1.click()

time.sleep(2)

notnow2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
notnow2.click()


time.sleep(2)

message = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
message.click()

time.sleep(2)

selection = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')
selection.click()

time.sleep(2)

who = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')
who.send_keys(mesajKisi)

time.sleep(2)

choise = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button')
choise.click()

time.sleep(2)

go = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button')
go.click()

time.sleep(2)

for i in range(0,10):
    write = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    write.send_keys(mesaj)
    write.send_keys(Keys.ENTER)

