# Created by ay27 at 16/10/9
import requests
from bs4 import BeautifulSoup


def check(keyword, title):
    return keyword in title


def craw_volume(href, keyword):
    volume_page = requests.get(href)
    ss = BeautifulSoup(volume_page.text, 'lxml')
    uls = ss.find_all(attrs={'class': 'publ-list'})

    volume_papers = []
    for ul in uls:
        for li in ul.find_all('li', attrs={'class': 'entry article'}):
            try:
                data = li.find('div', attrs={'class': 'data'})
                title = data.find('span', attrs={'class': 'title'}).text
                authors = []
                for author in data.find_all('span', attrs={'itemprop': 'author'}):
                    authors.append(author.text)
                paper_href = li.find('nav', attrs={'class': 'publ'}).ul.li.div.a.attrs['href']
                if check(keyword, title):
                    volume_papers.append([title, authors, paper_href])
            except:
                continue

    return volume_papers


def craw_journal(url, keyword):
    release_page = requests.get(url)
    soup = BeautifulSoup(release_page.text, "lxml")

    ul_tag = soup.find_all('ul')[12]
    volumes = []
    for li in ul_tag.find_all('li'):
        for a in li.find_all('a'):
            volumes.append([li.text, a.text, a.attrs['href']])

    # volumes[0].append(craw_volume(volumes[0][2]))
    # return volumes
    for volume in volumes:
        volume.append(craw_volume(volume[2], keyword))
    return volumes


def write_journal(year, volume_id, papers):
    with open('journal.md', 'a') as f:
        # year = year.replace('\n', '')
        f.write('## [%s\t%s]\n' % (year.split('\n')[0], volume_id.strip()))
        for paper in papers:
            f.write('**Title: %s**\nAuthor: %s\n<%s>\n\n' % (paper[0], paper[1], paper[2]))
