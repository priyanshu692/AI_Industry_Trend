import requests
from bs4 import BeautifulSoup


def search_company_industry(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for item in soup.find_all('h3'):
        link = item.find_parent('a')
        if link:
            title = item.get_text()
            url = link.get('href')
            results.append((title, url))

    return results


if __name__ == "__main__":
    company_info = search_company_industry("Automotive Industry AI")
    for info in company_info:
        print(info)
