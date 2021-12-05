"""
News scrapers
"""
import yaml
import requests
import urllib3
from bs4 import BeautifulSoup


def crawls_section(url):
    """
    Crawls the articles from one specific section of the website
    """
    import requests
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    from bs4 import BeautifulSoup

    import pandas as pd

    ## GET PAGE DATA
    req = urllib3.PoolManager()
    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')

    # Gets title blocks - retrieves Title and URLs from each
    headers = soup.find_all('header', {'class': 'entry-header'})

    titles, urls = [], []

    for header in headers:
        titles.append( header.find('img')['alt'] )
        urls.append( header.find('a')['href'] )

    df = pd.DataFrame({ 'title': titles, 'urls': urls })

    


    return df



def main():
    """
    Wrapper of the crawling pipeline
    """
    import yaml

    # Get the list of sections you want to crawl

    for url in urls:


    return None



if __name__ == '__main__':

    main()

    urls = [
        'https://www.ilpost.it/italia/',
        'https://www.ilpost.it/mondo/',
        'https://www.ilpost.it/politica/',
        'https://www.ilpost.it/economia/',
        'https://www.ilpost.it/europa/',
        'https://www.ilpost.it/internet/',
        'https://www.ilpost.it/scienza/'
    ]




    # TIME
    datetime = soup.find('meta', {'property': "article:published_time"})
    datetime = datetime['content']
    datetime = datetime[:10]

    # TITLE
    title = soup.find('meta', {'property': "og:title"})
    title = title['content']
    if "|" in title:
        title = re.split(r" \| ", title)[0]

    # SUBTITLE
    subtitle = soup.find('meta', {'property': "og:description"})
    subtitle = subtitle['content']
    subtitle = re.split(', says Guardian columnist', subtitle)[0]

    # BODY
    body = soup.find('div', {'class':"article-body-commercial-selector css-79elbk article-body-viewer-selector"})
    body = body.find_all('p')
    # body.find('p',class_='2').decompose()

    # for b in body: print(b)
    body = [ b.get_text() for b in body ]

    # check/remove last "[name] is a Guardian columnist"
    if body[-1].endswith('is a Guardian columnist'):
        body = body[:-1]

    body = ' '.join(body)
    body = re.sub(' +', ' ', body)

    article_dict = {
        'time': datetime,
        'title': title,
        'subtitle': subtitle,
        'body': body
    }
    return article_dict
