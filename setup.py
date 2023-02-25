from setuptools import setup, find_packages

setup(
    name='mtgoscraper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'mtgoscraper = mtgoscraper.main:main'
        ]
    }
)
