import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL for Steam top sellers search
base_url = "https://store.steampowered.com/search/results/?query&filter=topsellers&start={}&count=50"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

all_data = []

# Scrape first 5 pages (50 games per page)
for start in range(0, 250, 50):  # 0, 50, 100, 150, 200
    url = base_url.format(start)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    games = soup.find_all('a', {'class': 'search_result_row'})
    for game in games:
        name = game.find('span', {'class': 'title'}).text
        release = game.find('div', {'class': 'search_released'}).text
        price_span = game.find('div', {'class': 'search_price_discount_combined'})
        if price_span:
            price_text = price_span.get_text(strip=True)
            price = price_text.replace('\n', ' ').split(' ')[-1]
        else:
            price = "Free"

        rating_span = game.find('div', {'class': 'search_review_summary'})
        if rating_span and rating_span.has_attr('data-tooltip-html'):
            rating = rating_span['data-tooltip-html'].split('<br>')[0].strip()
        else:
            rating = "No rating"

        all_data.append([name, release, price, rating])

    time.sleep(1)  # polite scraping delay

# Create DataFrame
df = pd.DataFrame(all_data, columns=['Game Name', 'Release Date', 'Price', 'User Rating'])

# Save to CSV
df.to_csv("steam_top_games.csv", index=False)
print("CSV saved successfully as 'steam_top_games.csv'")