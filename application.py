from flask import Flask, render_template, send_from_directory
import random
import revelationnews

application = Flask(__name__, static_folder='static')

@application.route('/static/favicon.ico')
def fav():

    return send_from_directory(application.static_folder, 'favicon.ico')


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/blog')
def hello():
    return render_template('blog.html')


@application.route('/badtopic')
def choose_topic():

    dire_list = [
        'aboard', 'along', 'amid', 'beneath', 'beyond', 'concerning',
        'despite', 'except', 'following', 'like', 'minus', 'next',
        'onto', 'opposite', 'outside', 'past', 'per', 'plus', 'regarding',
    ]
    random.shuffle(dire_list)
    return render_template('badtopic.html', chosen_word=dire_list.pop())


@application.route('/revnews')
def RevNewsDisp():
    info_listed = revelationnews.new_search()

    return render_template('revnews.html',
                           chap_num=info_listed[0][0],
                           verse_num=info_listed[0][1],
                           cleaned_verse=info_listed[0][2],
                           topic=info_listed[1][0].upper(),
                           news_title=info_listed[1][1],
                           news_url=info_listed[1][2],
                           news_description=info_listed[1][3]
                           )


if __name__ == '__main__':
    application.run(debug=True)
