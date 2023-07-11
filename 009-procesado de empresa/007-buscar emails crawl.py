import re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def search_email_in_site(url, visited_pages=None):
    if visited_pages is None:
        visited_pages = set()

    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        return []

    visited_pages.add(url)

    # Search for email addresses in the current page
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails_found = re.findall(email_pattern, response.text)

    # Extract links from the page
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')

    for link in links:
        href = link.get('href')
        if href and href.startswith('http') and href not in visited_pages:
            emails_found.extend(search_email_in_site(href, visited_pages))

    return emails_found

# Example usage
url = 'https://enetres.net/'  # Replace with your target URL
emails = search_email_in_site(url)

if emails:
    print("Emails found in the website:")
    for email in emails:
        print(email)
else:
    print("No email addresses found in the website.")
