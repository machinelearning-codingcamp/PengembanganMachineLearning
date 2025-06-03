from bs4 import BeautifulSoup

title = "Guardians_of_the_Galaxy_Vol3" 
filename = f"Ant-Man and The Wasp_ Quantumania - Movie Reviews _ Rotten Tomatoes.html"

# Load the saved HTML file
with open(filename, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract reviews
reviews = soup.find_all('p', class_='audience-reviews__review js-review-text')

# Save reviews to a text file
output_filename = f"{title}_reviews.txt"
with open(output_filename, "w", encoding="utf-8") as file:
    for review in reviews:
        file.write(review.get_text(strip=True) + "\n")

print(f"✅ Extracted reviews saved to {output_filename}")
