import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = 'https://example.com'
response = requests.get(url)

# Parse the contents with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract data from the parsed contents
# For example, find all the links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
