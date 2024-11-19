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
        print("button vettisakyo dostt")

        # wait for few seconds before clicking
        time.sleep(1.5)
        nepse_chart_menu.click()

        #agian waiting for few seconds before clicking the charts
        time.sleep(1.6)
        chart_link_xpath = "//a[contains(@class, 'menu-item') and @href='/nepse-charts']"

        chart_link = driver.find_element(By.XPATH, chart_link_xpath)
        time.sleep(1)
        chart_link.click()


        nepse_index_xpath = "//span[@class='q-pr-xs text-h4']"

        time.sleep(1)
        driver.find_element(By.XPATH, nepse_index_xpath)
        print("Index pani vettiyoooooo")

        #now gonna scrape the website's content with beautiful soup

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        title = soup.find('title').text
        print(title)

        spans = soup.find_all('span')  #find_all returns span in list/array as there are many spans to return

        # for items in spans:  //printing all the spans as text
        #     print(items.text)

        print(spans[28].text) #locating the nepse index in find_all list

        nepse_index = spans[28].text

        with open("C:\\Users\\asus\\Desktop\\nepse.csv", mode="w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nepse:", nepse_index])

        # search_box_xpath = "//div[@class='js-button-text text-uO7HM85b text-rlvYsQ_k' and text()='NEPSE']"

        # WebDriverWait(driver,10).until(
        #     EC.presence_of_element_located((By.XPATH, search_box_xpath))
        # )
        # print("type handim? Vettiyo")    

        input("press enter to exit")



        driver.quit()
                
    except:
        print("Mission failed!")
    
    finally:
        driver.quit()



while True:
    print("Starting the scraping")
    scrape_chukul()
    print("waiting for 10 seconds before again scraping...")
    time.sleep(10)