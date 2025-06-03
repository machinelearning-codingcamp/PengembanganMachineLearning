from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
service = Service(r"D:\driver\chromedriver-win32\chromedriver.exe") 
driver = webdriver.Chrome(service=service, options=options)

movies = {
    # "Deadpool_N_Wolverine": "https://www.rottentomatoes.com/m/deadpool_and_wolverine/reviews?type=user",
    # "The_Marvels": "https://www.rottentomatoes.com/m/the_marvels/reviews?type=userr",
    "Guardians_of_the Galaxy_Vol3": "https://www.rottentomatoes.com/m/guardians_of_the_galaxy_vol_3/reviews?type=user",
    "Ant-Man_and_The_Wasp_Quantumania": "https://www.rottentomatoes.com/m/ant_man_and_the_wasp_quantumania/reviews?type=user",
    "Black_Panther_Wakanda_Forever": "https://www.rottentomatoes.com/m/black_panther_wakanda_forever/reviews?type=user",
    "Thor_Love_and_Thunder": "https://www.rottentomatoes.com/m/thor_love_and_thunder/reviews?type=user"
}

for title, url in movies.items():
    count = 0
    print(f"\nScraping reviews for: {title}...")

    driver.get(url)

    while True:
        try:
            load_more_button = driver.find_element(By.XPATH, "//rt-button[@data-qa='load-more-btn']")
            driver.execute_script("arguments[0].click();", load_more_button)
            count += 1
            print(f"current reload count : {count}")
            time.sleep(2)
        except:
            print(f"No more reviews to load for {title}.")
            break

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    reviews = soup.find_all('p', class_='audience-reviews__review js-review-text')

    filename = f"{title}_reviews.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for review in reviews:
            file.write(review.get_text(strip=True) + "\n")

    print(f"✅ {title} reviews saved to {filename}")

driver.quit()
print("\n🎉 All movies processed.")
