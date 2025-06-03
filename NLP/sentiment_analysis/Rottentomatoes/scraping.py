import requests
from bs4 import BeautifulSoup

url = "https://www.rottentomatoes.com/m/avengers_endgame/reviews?type=user"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

with open("soup_output.txt", "w", encoding="utf-8") as file:
    file.write(str(soup))

print("Soup saved to soup_output.txt")

reviews = soup.find_all('p', class_='audience-reviews__review js-review-text')

with open("reviews.txt", "w", encoding="utf-8") as file:
    for review in reviews:
        file.write(review.get_text(strip=True) + "\n\n")

print("Reviews saved to reviews.txt")