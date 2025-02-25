import requests
from bs4 import BeautifulSoup

base_url = 'https://stackoverflow.com/questions'
r_ques = requests.get(base_url, timeout=10).text
link_count = 0
def clear_links(links):
    global link_count
    parts = links.split('/')
    if len(parts) > 3:
        left_text = '/'.join(parts[3:])
        req_text = left_text.replace('-', ' ')
        link_count += 1
        return req_text
    return ""
def format_question_body_output(link_text, question_body, answer_body):
    global link_count
    if question_body:
        return f"{link_count}. {link_text}\n\n\nQuestion body:\n{question_body}\n\n\nAnswer : {answer_body}\n=============================================================================="
soup_ques = BeautifulSoup(r_ques, 'html.parser')
main_bar = soup_ques.find("div", id="mainbar")
links = main_bar.find_all("a", class_="s-link")
with open('stackoverflow_links.txt', 'w', encoding='utf-8') as file:
    for link in links:
        href = link.get('href')
        #print(href)
        if href:
            link_text = clear_links(href)
            full_url = 'https://stackoverflow.com' + href if href.startswith('/') else base_url + href
            r_ans = requests.get(full_url, timeout=10).text
            soop_ans = BeautifulSoup(r_ans, 'html.parser')
            post_body = soop_ans.find("div", class_="post-layout")
            question_body = None
            answer_body = None
            if post_body:
                #print(f"Found post body for {href}")
                question_body_elem = post_body.find("div", class_="s-prose js-post-body")
                if question_body_elem:
                    question_body = question_body_elem.get_text(strip=True)
                    
                answers = soop_ans.find_all("div", class_="answer")
                #print(f"Found {len(answers)} answers")
                
                for i, answer in enumerate(answers[:2], 1):
                    answer_body = answer.find("div", class_="s-prose js-post-body")
                    
            
            output = format_question_body_output(link_text, question_body, answer_body)
            file.write(output + "\n\n")
