import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import time

def search_aol(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    url = f"https://search.aol.com/aol/search?q={urllib.parse.quote(query)}"
    try:
        r = requests.get(url, headers=headers, timeout=12)
        if r.status_code != 200:
            return []
        
        soup = BeautifulSoup(r.text, 'html.parser')
        links = []
        for a in soup.find_all('a'):
            href = a.get('href', '')
            if href:
                if 'linkedin.com/jobs/view' in href:
                    links.append(href)
                elif 'RU=' in href:
                    match = re.search(r'RU=([^/&]+)', href)
                    if match:
                        actual_url = urllib.parse.unquote(match.group(1))
                        if 'linkedin.com/jobs/view' in actual_url:
                            links.append(actual_url)
        return list(set(links))
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    queries = {
        "APM Startup NCR": "\"Associate Product Manager\" (Gurgaon OR Noida OR Delhi) \"fresher\" OR \"0-1 years\" OR \"0-2\" -Airtel -Zomato -Blinkit -Sprinklr -Delhivery -Aurora -Taxmann -Urban linkedin jobs",
        "Product Analyst Startup NCR": "\"Product Analyst\" (Gurgaon OR Noida OR Delhi) \"fresher\" OR \"0-1 years\" OR \"0-2\" -INDmoney -Policybazaar -Paytm -SBNRI -MobiKwik linkedin jobs",
        "PMM Startup NCR": "\"Product Marketing\" OR \"Marketing Associate\" (Gurgaon OR Noida OR Delhi) \"fresher\" OR \"0-1 years\" OR \"0-2\" -Airtel -Pepperfry -Intozi linkedin jobs",
        "Consulting Strategy Startup NCR": "\"Strategy Analyst\" OR \"Consulting Analyst\" (Gurgaon OR Noida OR Delhi) \"fresher\" OR \"0-1\" -Accenture -EY -Cargill -ZS linkedin jobs",
        "Brand Executive Startup NCR": "\"Brand Executive\" OR \"Brand Assistant\" (Gurgaon OR Noida OR Delhi) \"fresher\" OR \"0-1\" -Cotecna -Reckitt -Nestle linkedin jobs"
    }
    
    all_found = {}
    for name, q in queries.items():
        print(f"\nSearching for: {name}...")
        urls = search_aol(q)
        print(f" -> Found {len(urls)} links.")
        if urls:
            all_found[name] = urls
        time.sleep(3)
        
    print("\n=== STARTUP SCRAPED RESULTS ===")
    for category, urls in all_found.items():
        print(f"\n{category}:")
        for u in urls[:5]:
            print(" -", u)
