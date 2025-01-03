# Method 1: Using a proxy API service (recommended)
# Create a new file: my_scraper/my_scraper/utils/proxy_fetcher.py

import requests
import json

def fetch_proxies_from_api():
    """
    Fetch proxies from a proxy API service.
    Replace API_KEY with your actual key.
    """
    api_url = "http://proxylist.geonode.com/api/proxy-list?limit=100&page=1&sort_by=lastChecked&sort_type=desc&filterUpTime=90&protocols=http%2Chttps&anonymityLevel=elite&anonymityLevel=anonymous"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        proxies = [f"http://{proxy['ip']}:{proxy['port']}" for proxy in data['data']]
        return proxies
    except Exception as e:
        print(f"Error fetching proxies: {e}")
        return []