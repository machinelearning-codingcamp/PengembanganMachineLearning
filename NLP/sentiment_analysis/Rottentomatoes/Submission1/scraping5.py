from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--headless=new")  # Run in headless mode
options.add_argument("--disable-gpu")  # Disable GPU rendering
options.add_argument("--enable-unsafe-swiftshader")  # Enable software rendering
options.add_argument("--disable-extensions")  # Remove extensions (fix TensorFlow issue)
options.add_argument("--no-sandbox")  # Fix potential crashes
options.add_argument("--disable-dev-shm-usage")  # Prevent memory crashes



service = Service(r"D:\driver\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

movies = {
    "Black_Panther_Wakanda_Forever": "https://www.rottentomatoes.com/m/black_panther_wakanda_forever/reviews?type=user",
    "Thor_Love_and_Thunder": "https://www.rottentomatoes.com/m/thor_love_and_thunder/reviews?type=user",
    "Doctor_Strange_in_the_Multiverse_of_Madness": "https://www.rottentomatoes.com/m/doctor_strange_in_the_multiverse_of_madness/reviews?type=user",
    "Spider-Man_No_Way_Home": "https://www.rottentomatoes.com/m/spider_man_no_way_home/reviews?type=user",
    "Eternals": "https://www.rottentomatoes.com/m/eternals/reviews?type=user",
}

for title, url in movies.items():
    print(f"\n🚀 Scraping reviews for: {title}...")

    start_time = time.time()
    last_click_time = start_time 
    retry_attempts = 3

    for attempt in range(retry_attempts):
        try:
            driver.get(url)
            time.sleep(5)  
            break 
        except Exception as e:
            print(f"⚠️ Error loading page ({attempt+1}/{retry_attempts}): {e}")
            time.sleep(10)  
    else:
        print(f"❌ Failed to load {title} after {retry_attempts} attempts. Skipping.")
        continue  

    count = 0
    while True:
        if time.time() - start_time > 2700: 
            print(f"⏳ Time limit reached for {title}. Moving on...")
            break

        try:
            load_more_button = driver.find_element(By.XPATH, "//rt-button[@data-qa='load-more-btn']")
            driver.execute_script("arguments[0].click();", load_more_button)
            count += 1
            print(f"🔄 Clicked 'Load More' ({count})")
            last_click_time = time.time()
            time.sleep(2)
        except:
            if time.time() - last_click_time > 180:
                print(f"🚫 No new reviews loaded in 3 minutes. Stopping for {title}.")
                break
            print(f"✅ No more 'Load More' button for {title}. Extracting reviews...")
            break

    soup = BeautifulSoup(driver.page_source, "html.parser")
    reviews = soup.find_all("p", class_="audience-reviews__review js-review-text")

    filename = f"{title}_reviews.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for review in reviews:
            file.write(review.get_text(strip=True) + "\n")

    print(f"✅ {title} reviews saved to {filename}")

driver.quit()
print("\n🎉 All movies processed.")
