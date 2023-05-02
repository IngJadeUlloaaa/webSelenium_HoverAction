import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')
driver.get('https://www.google.com')
time.sleep(3)
element = driver.find_element(By.LINK_TEXT, 'Publicidad')
time.sleep(3)
move_mouse = ActionChains(driver).move_to_element(element)
move_mouse.perform()
time.sleep(3)