import json
import requests
import random

# API.Bible credentials: f208fb25f01350215cb19b257fb1caf5
# API.Bible King James (Authorized) Version (protestant) ID: de4e12af7f28f599-02



def choose_rand_chap():
    """ Pick a random chapter from Revelation """
    return random.randint(1, 21)


def call_api_bible_chap(chap_num):
    """ Grab the chapter from the api.bible website and count the verses """
    bible_ver = 'de4e12af7f28f599-02'
    ref = f'REV.{chap_num}'

    headers = {
        'accept': 'application/json',
        'api-key': 'f208fb25f01350215cb19b257fb1caf5'
    }

    api_bible_response = requests.get(f'https://api.scripture.api.bible/v1/'
                                      f'bibles/{bible_ver}/chapters/{ref}/verses',
                                      headers=headers)
    # print(api_bible_response)
    api_bible_response_json = api_bible_response.json()["data"]
    # print(api_bible_response_json)
    chap_length = len(api_bible_response_json)

    return chap_length


def choose_rand_verse(chap_length):
    """" Pick a random verse from the chapter """
    return random.randint(1, chap_length)


def call_api_bible_verse(chap_num, verse_num):
    """" Grab the verse from the api.bible website """
    bible_ver = 'de4e12af7f28f599-02'
    ref = f'REV.{chap_num}.{verse_num}'

    params = 'content-type=text' \
             '&include-notes=false' \
             '&include-titles=true' \
             '&include-chapter-numbers=false' \
             '&include-verse-numbers=false' \
             '&include-verse-spans=false' \
             '&use-org-id=false'

    headers = {
        'accept': 'application/json',
        'api-key': 'f208fb25f01350215cb19b257fb1caf5'
    }

    api_bible_response = requests.get(f'https://api.scripture.api.bible/v1/'
                                      f'bibles/{bible_ver}/verses/{ref}?{params}',
                                      headers=headers)

    api_bible_response_json = api_bible_response.json()["data"]
    verse_str = api_bible_response_json["content"]

    return verse_str


def words_list_creation():
    """" Create a list of important words from the verse """
    words = []
    return words


def call_news_site(words):
    """ Search for news articles related to the verse """


# if __name__ == "__main__":
chap_num = choose_rand_chap()
print(f'REVELATION\nChapter {chap_num}')
chap_length = call_api_bible_chap(chap_num)
verse_num = choose_rand_verse(chap_length)
print(f'Verse {verse_num}')
verse_str = call_api_bible_verse(chap_num, verse_num)
print(verse_str)
