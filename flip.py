import requests
from bs4 import BeautifulSoup
base_url = 'https://www.flipkart.com/search?q='
product = str(input("Enter product name : "))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
full_url = base_url + product
r = requests.get(full_url, headers=headers, timeout=10)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')
links = set()
for a_tag in soup.find_all('a', href=True):
    if "/p/" in a_tag["href"]:
        links.add("https://www.flipkart.com" + a_tag["href"])
with open('flipkart_links.txt', 'w') as file:
    for link in links:
        file.write(link + "\n")