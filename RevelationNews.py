import requests
import random

# API.Bible credentials: f208fb25f01350215cb19b257fb1caf5
# API.Bible King James (Authorized) Version (protestant) ID: de4e12af7f28f599-02

# https://api.ap.org/media/v/content/search?q=versioncreated:2018-01-19&apikey={apikey}


def call_api_bible():
    """" Grab the verse from the api.bible website """
    bible_version = 'de4e12af7f28f599-02'
    headers = {
        'accept': 'application/json',
        'api-key': 'f208fb25f01350215cb19b257fb1caf5'
    }

    api_bible_response = requests.get(f'https://api.scripture.api.bible/v1/bibles/{bible_version}/verses/', headers=headers)

    print(api_bible_response.json())


def words_list_creation():
    """" Create a list of important words from the verse"""
    words = []
    return words


def call_news_site(words):
    """ Search for news articles related to the verse"""


if __name__ == "__main__":
    call_api_bible()
