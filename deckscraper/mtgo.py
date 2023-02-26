import requests
import json
from bs4 import BeautifulSoup


def find_decklists_data_row(rows):
    for line in rows.split('\n'):
        # MTGO website assigns the decklist data to window object
        # using JavaSript, scan for that line from the website source
        if 'window.MTGO.decklists.data' in line:
            return line
    return None


def strip_parseable_json(row):
    # Remove any leading or trailing whitespace
    output = row.strip()

    # Remove the javascript assignment to window object
    output = output.removeprefix('window.MTGO.decklists.data = ')

    # Remove the javascript ';' from the end of the line
    output = output.removesuffix(';')

    return output


def scrape_tournament_results(url):
    response = requests.get(url)

    raw_data = find_decklists_data_row(response.text)
    if raw_data is None:
        print('Error finding decklist data from page')
        return None

    json_str = strip_parseable_json(raw_data)

    try:
        tournament_results = json.loads(json_str)
        return tournament_results
    except json.decoder.JSONDecodeError as e:
        print('Error parsing JSON: {}'.format(e))
        return None


def scrape_latest_tournament_links():
    base_link = 'https://www.mtgo.com'
    response = requests.get(base_link + "/en/mtgo/decklists")

    soup = BeautifulSoup(response.content, 'html.parser')
    links = []

    container = soup.find('ul', {'class': 'decklists-list'})

    for item in container.find_all('li', {'class': 'decklists-item'}):
        # Get the link of the decklist
        link = item.find('a', {'class': 'decklists-link'})['href'].strip()

        # Get the name of the link
        name = item.find('h3').text.strip()

        # Get the format by checking the icon's class
        icon = item.find('div', {'class': 'decklists-icon'})
        try:
            game_format = icon['class'][1]
        except IndexError:
            game_format = 'unknown'

        # Get the date of the link
        day = item.find('span', {'class': 'day'}).text.strip()
        month = item.find('span', {'class': 'month'}).text.strip()
        year = item.find('span', {'class': 'year'}).text.strip()

        # Add the decklist to the list of decklists
        links.append({'link': base_link + link, 'name': name, 'format': game_format,
                      'day': day, month: 'month', year: 'year'})

    return links
