import time
from bs4 import BeautifulSoup
import re

# def get_rating()

def get_problems_solved(driver, username):
    url = f'https://leetcode.com/{username}'
    problems_leetcode = []
    driver.get(url)
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract the titles of the most recent problems solved
    div = soup.find_all('div', attrs={'data-title': True})
    rating = soup.find
    for i in div:
        children = i.findChildren('span')
        pattern = r'^(a\ minute\ ago|a\ few\ seconds\ ago|an\ hour\ ago|\d+\ hours\ ago|\d+\ minutes\ ago)$'
        match = re.search(pattern, children[1].text)
        # concatenate the link with the base url
        if match:
            submission_link = f"https://leetcode.com{i.parent['href']}"
            problem_link = f"https://leetcode.com/problems/{i['data-title'].lower().replace(' ', '-')}/"
            submission_id = i.parent['href'].split('/')[-2]
            problems_leetcode.append({ 'problem_title':  i['data-title'], 'problem_link': problem_link, 'submission_link': submission_link, 'submission_id':submission_id, 'platform': 'Leetcode', 'username': username, 'current_rating': rating })
        else:
            break

    return problems_leetcode