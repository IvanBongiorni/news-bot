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

    # Get page data
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
    params = yaml.load(open(os.getcwd() + '/config.yaml'), yaml.Loader)

    df_new= []
    df_old = pd.read_csv(os.path.join(os.getcwd(), 'history', 'history_ilpost.csv'))

    for url in urls:
        current_df_new, current_df_old = crawls_section(url)
        df_new.append(current_df_new)

    df_new = pd.concat(df_new)

    # Substitute old .csv with new one, filter out
    df_new.to_csv(os.path.join(os.getcwd(), 'history', 'history_ilpost.csv'), index=False)
    df_new = df_new[ ~df_new['urls'].isin(df_new['urls'])
    df_new['source'] = 'Il Post'

    return df_new


if __name__ == '__main__':
    main()
