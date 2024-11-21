import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv

from bs4 import BeautifulSoup

def scrape_chukul():
    try:
        driver = webdriver.Chrome()

        driver.get("https://chukul.com/")

        chart_xpath = "//div[@class='q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable' and @role='button' and contains(@aria-label, 'Expand')]//div[contains(text(), 'Nepse Chart')]"

        nepse_chart_menu = driver.find_element(By.XPATH, chart_xpath)
      

        # wait for few seconds before clicking
        time.sleep(1.5)
        nepse_chart_menu.click()

        #agian waiting for few seconds before clicking the charts
        time.sleep(1.6)
        chart_link_xpath = "//a[contains(@class, 'menu-item') and @href='/nepse-charts']"

        chart_link = driver.find_element(By.XPATH, chart_link_xpath)
        time.sleep(1)
        chart_link.click()
        
        #identifying nepes's index through html xpath
        nepse_index_xpath = "//span[@class='q-pr-xs text-h4']"

        time.sleep(1)
        driver.find_element(By.XPATH, nepse_index_xpath)

        #now gonna scrape the website's content with beautiful soup
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        title = soup.find('title').text
        print(title)
        
        spans = soup.find_all('span')  #find_all returns span in list/array as there are many spans to return

        print(spans[28].text) #locating the nepse index in find_all list

        nepse_index = spans[28].text #storing the nepse point in nepse_index
        
        #writing the nepse index in a csv file
        with open("C:\\Users\\asus\\Desktop\\nepse.csv", mode="w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nepse:", nepse_index])

        input("press enter to exit")
        
        driver.quit()
                
    except:
        print("Mission failed!")
        

while True:
    print("Starting the scraping")
    scrape_chukul()
    print("waiting for 10 seconds before again scraping...")
    time.sleep(15) #running the program every 10 seconds