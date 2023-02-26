# Python MTGO decklists scraper

A simple scraper library for extracting decklists from MTGO website.

## Installation

```bash
pip install git+https://github.com/Cadiac/python-mtg-decks-scraper.git
```

## Usage

```python
from deckscraper import mtgo

links = mtgo.latest_tournament_links()
url = links[0]['link']
results = mtgo.tournament_results(url)
```

## Development

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -e '.[dev]'
$ pytest
```