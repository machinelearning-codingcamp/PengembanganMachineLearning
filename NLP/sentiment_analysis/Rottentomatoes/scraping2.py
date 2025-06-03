from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
service = Service(r"D:\driver\chromedriver-win32\chromedriver.exe") 
driver = webdriver.Chrome(service=service, options=options)

# Open the webpage

# Marvel endgame URL
# url = r"https://www.rottentomatoes.com/m/avengers_endgame/reviews?type=user"
# Marvel Spiderman Far from Home URL 
# url = r"https://www.rottentomatoes.com/m/spider_man_far_from_home/reviews?type=user" 
# Avengers: Infinity War URL
# url = r"https://www.rottentomatoes.com/m/avengers_infinity_war/reviews?type=user" 
# Captain Marvel URL
url = r"https://www.rottentomatoes.com/m/captain_marvel/reviews?type=user" 
driver.get(url)

while True:
    try:
        load_more_button = driver.find_element(By.XPATH, "//rt-button[@data-qa='load-more-btn']")
        driver.execute_script("arguments[0].click();", load_more_button)
        time.sleep(2) 
    except:
        print("No more reviews to load.")
        break

soup = BeautifulSoup(driver.page_source, 'html.parser')

reviews = soup.find_all('p', class_='audience-reviews__review js-review-text')

# with open("reviews.txt", "w", encoding="utf-8") as file:
# with open("SMFHreviews.txt", "w", encoding="utf-8") as file:
# with open("CMWreviews.txt", "w", encoding="utf-8") as file:
with open("CMreviews.txt", "w", encoding="utf-8") as file:
    for review in reviews:
        file.write(review.get_text(strip=True) + "\n")

driver.quit()

print("All reviews saved txt")
