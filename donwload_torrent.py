import requests
from bs4 import BeautifulSoup
import subprocess




url='www.btbtt19.com'
response=requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')

# Find the <a> tags that contain the .torrent file links
torrent_links = soup.find_all('a', href=lambda href: href and href.endswith('.torrent'))