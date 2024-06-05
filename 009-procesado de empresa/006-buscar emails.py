import re
import requests

def search_email_in_source(url):
    # Retrieve the web page source code
    response = requests.get(url)
    source_code = response.text

    # Search for email addresses using regular expressions
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails_found = re.findall(email_pattern, source_code)

    return emails_found

# Example usage
url = 'https://enetres.net/'  # Replace with your target URL
emails = search_email_in_source(url)

if emails:
    print("Emails found in the source code:")
    for email in emails:
        print(email)
else:
    print("No email addresses found in the source code.")
