from setuptools import setup, find_packages

setup(
    name='mtgoscraper',
    version='0.1.0',
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
    },
    entry_points={
        'console_scripts': [
            'mtgoscraper = mtgoscraper.main:main'
        ]
    }
)
