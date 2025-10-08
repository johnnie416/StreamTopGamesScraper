# Steam Top Games Scraper

A Python web scraper that collects top-selling games on Steam and exports the data to a CSV file.

## Features
- Scrapes multiple pages of Steam top sellers.
- Extracts:
  - Game Name
  - Release Date
  - Price
  - User Rating
- Cleans and formats data.
- Saves results to steam_top_games.csv.

## Technologies Used
- Python
- Requests
- BeautifulSoup4
- Pandas

## How to Use
1. Clone the repository:
   `bash
   git clone https://github.com/johnnie416/StreamTopGamesScraper.git

2. Install dependencies:

pip install requests beautifulsoup4 pandas


3. Run the scraper:

python steam_scraper.py


4. Check steam_top_games.csv for the results.