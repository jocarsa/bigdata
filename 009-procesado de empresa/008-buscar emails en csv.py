import re
import requests
import csv

def search_email_in_source(url):
    # Retrieve the web page source code
    response = requests.get(url)
    source_code = response.text

    # Search for email addresses using regular expressions
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails_found = re.findall(email_pattern, source_code)

    return emails_found

# Open the CSV file
with open('empresas.csv', 'r') as csvfile:
    archivo = open("empresasycorreos2.csv",'a')
    reader = csv.reader(csvfile)

    for row in reader:
        print(row)
        # Example usage
        url = row[1]  # Replace with your target URL
        try:
            emails = search_email_in_source(url)

            if emails:
                print("Emails found in the source code:")
                for email in emails:
                    print(email)
                    
                    archivo.write(row[0]+","+row[1]+","+email+"\n")
                    
            else:
                print("No email addresses found in the source code.")
        except Exception as e:
            print(e)
    archivo.close()

