import requests
from bs4 import BeautifulSoup
import pandas as pd

start_url = 'https://en.wikipedia.org/wiki/Main_Page'

downloaded_html = requests.get(start_url)

soup = BeautifulSoup(downloaded_html.text)

with open('download.html', 'w') as file:
    file.write(soup.prettify())