from mtgoscraper import scrape_tournament_results


def test_scrape_decklists():
    url = 'https://www.mtgo.com/en/mtgo/decklist/legacy-preliminary-2023-02-2312525215'
    results = scrape_tournament_results(url)
    assert len(results['decks']) == 4
