import requests
import pprint
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')

# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)
# print(soup.body)
# print(soup.find_all('a'))  => finds all the a tags
# print(soup.select('.score'))      => allows us to search css ids and classes

links = soup.select('.storylink')
subtext = soup.select('.subtext')

# print(links[0], votes[0])

def sort_by_votes(hn):
    return sorted(hn, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'href': href, 'votes': points})
    return sort_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))