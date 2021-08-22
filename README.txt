           __
        __/  \__
   ____/________\____
   |----------------|
   | RevelationNews |
   |----------------|
   |    v 0.1.0     |
   |   2021-08-22   |
------------------------
------------------------


1. Table of Contents
    1. Table of Contents
    2. About the Program
    3. List of Files
    4. Requirements
    5. Instructions
    6. About the Author
    7. To-Do List


2. About the Program
          This webpage displays a random verse from the book of
          Revelation and then gives a link to a "related" news
          article from the past few months.

          It uses Python, Flask, and AWS Elastic Beanstalk


3. List of Files:
    + templates/
        + badtopic.html
        + blog.html
        + index.html
        + revnews.html
    + application.py
    + README.txt 
    + requirements.txt
    + revelationnews.py


4. Requirements:
    + Python 3 (developed in 3.7.4)
        Modules:
        -flask
        -re
        -requests
        -random

    + Internet connection
        API Dependencies:
        -scripture.api.bible
        -newsapi.org


5. Instructions:
    + Create 'keychain.py' and write python functions that return your api key for 'bible' and 'news'
    + Run application.py for localhosting
    + Alternatively:
        + Create an AWS Elastic Beanstalk environment for Python w/ Flask
        + Compress the entire RevNews directory 
        + Upload the .zip to the env

6. About the Author
    Canyon Read
        Cloud Systems Consultant
        B.A. Strategic Communication - Washington Sate University
        San Jose, California, United States of America


7. To-Do List
    o Better management of the dire list and chap-verse dictionary
    o Run program as AWS Lambda instead of using an EC2 (?)
    o Make better interface (using .js)
    o Add save button and database to store 'favorite results' (?)
    o Fix favicon not loading