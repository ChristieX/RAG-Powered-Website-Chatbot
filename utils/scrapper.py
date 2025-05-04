import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape_website(url, max_pages=10):
    visited = set()
    content_list = []

    def crawl(u):
        if u in visited or len(visited) >= max_pages:
            return
        visited.add(u)
        try:
            resp = requests.get(u, timeout=5)
            soup = BeautifulSoup(resp.text, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)
            content_list.append(text)

            for link in soup.find_all('a', href=True):
                next_url = urljoin(u, link['href'])
                if urlparse(next_url).netloc == urlparse(url).netloc:
                    crawl(next_url)
        except Exception as e:
            print(f"Failed to fetch {u}: {e}")

    crawl(url)
    return content_list
