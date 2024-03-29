import requests
from bs4 import BeautifulSoup
import re

# URL you want to scrape
url = 'https://www.cdc.gov/measles/cases-outbreaks.html'

state_cases = {
    'AL': 0,
    'AK': 0,
    'AZ': 0,
    'AR': 0,
    'CA': 0,
    'CO': 0,
    'CT': 0,
    'DE': 0,
    'FL': 0,
    'GA': 0,
    'HI': 0,
    'ID': 0,
    'IL': 0,
    'IN': 0,
    'IA': 0,
    'KS': 0,
    'KY': 0,
    'LA': 0,
    'ME': 0,
    'MD': 0,
    'MA': 0,
    'MI': 0,
    'MN': 0,
    'MS': 0,
    'MO': 0,
    'MT': 0,
    'NE': 0,
    'NV': 0,
    'NH': 0,
    'NJ': 0,
    'NM': 0,
    'NY': 0,
    'NC': 0,
    'ND': 0,
    'OH': 0,
    'OK': 0,
    'OR': 0,
    'PA': 0,
    'RI': 0,
    'SC': 0,
    'SD': 0,
    'TN': 0,
    'TX': 0,
    'UT': 0,
    'VT': 0,
    'VA': 0,
    'WA': 0,
    'WV': 0,
    'WI': 0,
    'WY': 0
}

for states in state_cases:
    # Send a HTTP request to the specified URL
    response = requests.get(url)

    # Parse the response content with Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Search for a paragraph containing "Measles cases in 2024"
    paragraphs = soup.find_all('h2')
    for paragraph in paragraphs:
        if "Measles cases in 2024" in paragraph.text:
            next_paragraph = paragraph.find_next_sibling('p')
            if next_paragraph:
                print(next_paragraph.text)  # This prints the number of cases
                break
