import re
import requests
import random


def choose_rand_chap():
    """ Pick a random chapter from Revelation """
    return random.randint(1, 21)


def find_chap_len(chap_num):
    """ Determine the length of the chapter """
    chapter_lengths = {
        1: 20, 2: 29, 3: 22, 4: 11, 5: 14, 6: 17, 7: 17,
        8: 13, 9: 21, 10: 11, 11: 19, 12: 17, 13: 18, 14: 20,
        15: 8, 16: 21, 17: 18, 18: 24, 19: 21, 20: 15, 21: 27, 22: 21
    }
    return(chapter_lengths[chap_num])


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

    # This could probably be its own function for parsing the verse from the response:
    api_bible_response_json = api_bible_response.json()["data"]
    verse_str = api_bible_response_json["content"]


    return verse_str


def clean_verse_up(verse_str):
    """ Remove the spaces before and the line break after the verse """

    while verse_str[0] == " ":
        verse_str = verse_str[1:]

    verse_str = verse_str[:-1]

    return verse_str


def words_list_creation(verse_str):
    """" Create a list of important words from the verse """

    dire_list = [
        'and', 'or', 'nor', 'so', 'yet', 'he', 'also', 'let',
        'although', 'far', 'if', 'long', 'soon', 'though', 'because',
        'considering', 'either', 'however', 'order', 'that', 'neither',
        'so', 'then', 'unless', 'when', 'whenever', 'where',
        'whereas', 'wherever', 'whether', 'while', 'did',
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
    """ Pick a word to be the topic of the news article """
    random.shuffle(words)
    return words.pop()


def call_news_api(topic):
    """ Search for news articles related to the verse """

    params = f'qInTitle={topic}' \
             '&language=en' \
             '&include-titles=true' \
             '&sortBy=relevancy' \
             '&pageSize=1' \
             '&apiKey=#####'

    news_api_response = requests.get(f"https://newsapi.org/v2/everything?{params}")


    # This could probably be its own function for parsing the response:
    news_api_response_json = news_api_response.json()['articles'][0]
    # print(news_api_response_json)
    # news_source = news_api_response_json['source']
    news_title = news_api_response_json['title']
    news_url = news_api_response_json['url']
    news_description = news_api_response_json['description']

    # This could probably be its own function for printing the news info:
    print(news_title)
    # print(news_source['name'])
    print(news_description)
    print(news_url)


# if __name__ == "__main__":
chap_num = choose_rand_chap()
chap_length = find_chap_len(chap_num)
verse_num = choose_rand_verse(chap_length)
print(f'REVELATION\nChapter {chap_num}\nVerse {verse_num}')
verse_str = call_api_bible_verse(chap_num, verse_num)
print(clean_verse_up(verse_str))
words = words_list_creation(verse_str)
# print(words)
topic = choose_topic(words)
print(topic.upper())
call_news_api(topic)
