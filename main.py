import requests
from bs4 import BeautifulSoup
r = requests.get('https://stackoverflow.com/questions', timeout=10).text
link_count = 0
def clear_links(links):
    global link_count
    parts = links.split('/')
    if len(parts) > 3:
        left_text = '/'.join(parts[3:])
        req_text = left_text.replace('-', ' ')
        link_count += 1
        return f"{link_count}. {req_text}"
    return ""
soup = BeautifulSoup(r, 'html.parser')
main_bar = soup.find("div", id="mainbar")
links = main_bar.find_all("a", class_="s-link")
with open('stackoverflow_links.txt', 'w', encoding='utf-8') as file:
	for link in links:
		href = link.get('href')
		if href:
			processed_text = clear_links(href)
		file.write(processed_text + '\n')