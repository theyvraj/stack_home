import requests
from bs4 import BeautifulSoup
r =  requests.get('https://stackoverflow.com/questions', timeout=10).text

def clear_links(links):
    parts = links.split('/')
    if len(parts) > 3:
        left_text = '/'.join(parts[3:])
        req_text = left_text.replace('-', ' ')
        return req_text
soup = BeautifulSoup(r, 'html.parser')
main_bar = soup.find("div", id="mainbar")
links = main_bar.find_all("a", class_="s-link")
for link in links:
    href = link.get('href')
    if href:
        processed_text = clear_links(href)
    print(processed_text)