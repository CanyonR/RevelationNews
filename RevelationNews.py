import re
import requests
import random

# API.Bible key: #####
# newsapi.org key: #####


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
        'api-key': '#####'
    }

    api_bible_response = requests.get(f'https://api.scripture.api.bible/v1/'
                                      f'bibles/{bible_ver}/verses/{ref}?{params}',
                                      headers=headers)

    api_bible_response_json = api_bible_response.json()["data"]
    verse_str = api_bible_response_json["content"]
    # print(api_bible_response_json)

    return verse_str


def words_list_creation(verse_str):
    """" Create a list of important words from the verse """

    dire_list = [
        'and', 'or', 'nor', 'so', 'yet', 'he', 'also', 'let',
        'although', 'far', 'if', 'long', 'soon', 'though', 'because',
        'considering', 'either', 'however', 'order', 'that', 'neither',
        'so', 'then', 'unless', 'when', 'whenever', 'where',
        'whereas', 'wherever', 'whether', 'while',
        'about', 'above', 'across', 'against', 'among', 'around', 'at',
        'behind', 'below', 'beside', 'between', 'by', 'down', 'during',
        'from', 'inside', 'into', 'near', 'of', 'off', 'on', 'out',
        'over', 'through', 'to', 'toward', 'under', 'up', 'with',
        'aboard', 'along', 'amid', 'beneath', 'beyond', 'concerning',
        'despite', 'except', 'following', 'like', 'minus', 'next',
        'onto', 'opposite', 'outside', 'past', 'per', 'plus', 'regarding',
        'round', 'save', 'till', 'underneath', 'unlike', 'upon', 'versus',
        'via', 'within', 'without', 'as', 'but', 'since', 'than', 'until',
        'alas', 'saying', 'in', 'the', 'a', 'an', 'they', 'them', 'their',
        'where', 'wherein', 'had', 'has', 'have', 'for', 'is', 'was',
        'were', 'i', 'me', 'my', 'you', 'your', 'our', 'ours', 'it',
        'here', 'there', 'his', 'him', 'she', 'hers', 'unto', 'part',
        'ye', 'which', 'come', 'things', 'are', 'shall', 'be', 'day',
        'night', 'ever', 'not', 'no', 'yes', 'should', 'would', 'her',
        'he', 'set', 'who', 'whom', 'see', 'said', 'am', 'will', 'after',
        'must', 'all', 'some', 'many', 'few', 'what', 'make', 'went',
        'came', 'this', 'that', 'these', 'made'
    ]

    words_all = re.sub("[^\w]", " ", verse_str.lower()).split()
    words_important = []

    for word in words_all:
        if word not in dire_list:
            words_important.append(word)

    return words_important


def choose_topic(words):
    """ Search for news articles related to the verse """
    random.shuffle(words)
    return words.pop()


def call_news_site(topic):
    """ Search for news articles related to the verse """

    params = f'qInTitle={topic}' \
             '&language=en' \
             '&include-titles=true' \
             '&sortBy=relevancy' \
             '&pageSize=1' \
             '&apiKey=#####'


    news_api_response = requests.get(f"https://newsapi.org/v2/everything?{params}")

    news_api_response_json = news_api_response.json()['articles'][0]
    # print(news_api_response_json)
    news_source = news_api_response_json['source']
    news_title = news_api_response_json['title']
    news_url = news_api_response_json['url']
    news_description = news_api_response_json['description']

    print(news_title)
    print(news_source['name'])
    print(news_description)
    print(news_url)



# if __name__ == "__main__":
chap_num = choose_rand_chap()
print(f'REVELATION\nChapter {chap_num}')
chap_length = call_api_bible_chap(chap_num)
verse_num = choose_rand_verse(chap_length)
print(f'Verse {verse_num}')
verse_str = call_api_bible_verse(chap_num, verse_num)
print(verse_str)
words = words_list_creation(verse_str)
# print(words)
topic = choose_topic(words)
print(topic.upper())
call_news_site(topic)
