import deckscraper.mtgo as mtgo


def test_scrape_tournament_results():
    url = 'https://www.mtgo.com/en/mtgo/decklist/legacy-preliminary-2023-02-2312525215'
    results = mtgo.scrape_tournament_results(url)
    assert len(results['decks']) == 4


def test_scrape_latest_tournament_links():
    results = mtgo.scrape_latest_tournament_links()
    assert len(results) > 0
