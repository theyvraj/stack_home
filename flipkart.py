import requests
from bs4 import BeautifulSoup
base_url = 'https://www.flipkart.com/search?q='
product = str(input("Enter product name : "))
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
end = '&sort=relevance'
full_url = base_url + product + end
r = requests.get(full_url, headers=headers, timeout=10)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')
links = set()
a_tags = soup.find_all(class_=["WKTcLC BwBZTg", "WKTcLC"])
for a in a_tags:
    title = a.find_previous_sibling()
    print(title)
    href = a.get('href')
    if href and "/p/" in href:
        full_link = "https://www.flipkart.com" + href
        links.add(full_link)
with open('flipkart_links.txt', 'w') as file:
    for i, link in enumerate(links, start=1):
        file.write(f"{i}. {title} {link} + \n")