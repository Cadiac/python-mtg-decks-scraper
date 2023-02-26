from setuptools import setup, find_packages

setup(
    name='deckscraper',
    version='0.1.0',
    description='A simple web scraper for MTG decklists',
    author='Jaakko Husso',
    url='https://github.com/Cadiac/python-mtgo-decks-scraper',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov'
        ]
    }
)
