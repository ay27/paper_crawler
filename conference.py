# Created by ay27 at 16/10/9
import requests
from bs4 import BeautifulSoup


def check(keyword, title):
    return keyword in title

def craw_workshop(href, keyword):
    workshop_page = requests.get(href)
    ss = BeautifulSoup(workshop_page.text, 'lxml')
    uls = ss.find_all(attrs={'class': 'publ-list'})

    workshop_papers = []
    for ul in uls:
        for li in ul.find_all('li', attrs={'class': 'entry editor'}):
            try:
                data = li.find('div', attrs={'class': 'data'})
                title = data.find('span', attrs={'class': 'title'}).text
                authors = []
                for author in data.find_all('span', attrs={'itemprop': 'author'}):
                    authors.append(author.text)
                paper_href = li.find('nav', attrs={'class': 'publ'}).ul.li.div.a.attrs['href']
                if check(keyword, title):
                    workshop_papers.append([title, authors, paper_href])
            except:
                continue
    return workshop_papers


def craw_conference(url, keyword):
    conf_page = requests.get(url)
    soup = BeautifulSoup(conf_page.text, 'lxml')

    conferences = []
    uls = soup.find_all('ul', attrs={'class': 'publ-list'})
    for ul in uls:
        for li in ul.find_all('li', attrs={'class': 'entry editor'}):
            data = li.find('div', attrs={'class': 'data'})
            workshop_title = data.find('span', attrs={'class': 'title'}).text
            workshop_href = data.find('a', text='[contents]').attrs['href']
            conferences.append([workshop_title, craw_workshop(workshop_href, keyword)])
            break
        break
    return conferences


def write_conference(workshop_title, papers):
    with open('conference.md', 'a') as f:
        # year = year.replace('\n', '')
        f.write('## [%s]\n' % workshop_title)
        for paper in papers:
            f.write('**Title: %s**\nAuthor: %s\n<%s>\n\n' % (paper[0], paper[1], paper[2]))
