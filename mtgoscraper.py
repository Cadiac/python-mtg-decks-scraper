import requests
import json


def find_decklists_data_row(rows):
    for line in rows.split('\n'):
        # MTGO assigns the decklist data to window object using JavaSript,
        # scan for that line from the website source
        if "window.MTGO.decklists.data" in line:
            return line
    return None


def strip_parseable_json(row):
    # Remove any leading or trailing whitespace
    output = row.strip()

    # Remove the javascript assignment to window object
    output = output.removeprefix("window.MTGO.decklists.data = ")

    # And the javascript ";" from line end
    output = output.removesuffix(";")

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
