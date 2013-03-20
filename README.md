# Introduction
This is an IRC bot built with Django. It uses yardbird as the IRC framework.

# Developing
This software was developed using python and virtualenv. You should be able to get it running anywhere, provided you can run python. Linux and OSX are probably the easiest options.

Virtualenv allows you to install python libraries for a single python application only. This way, there are no conflicts between this application and python libraries provided by your operating system. For more information on virtualenv, see this tutorial: http://simononsoftware.com/virtualenv-tutorial/. You'll want to install virtualenv and virtualenvwrapper on your OS. Doing this is not in the scope of this document

Create the virtualenv:

    mkvirtualenv bot

First clone this repository:

    git clone git@bitbucket.org:japz/bot.git
    
Work on the bot virtualenv:

    workon bot

Install all the required libraries for this project:

    pip install -r requirements.txt

Create the test database (you will be prompted for a username and password, you can use these to access the django built-in admin):

    cd src; ./manage.py syncdb; ./manage.py migrate

You can also modify the settings used in development. Most likely, you'll want to edit at least the IRC parameters in bot/settings.py.

Now, run the bot:

    ./manage.py runircbot

Also run the web interface:

    ./manage.py runserver


# Contributing

Contributing to this project is done by opening pull requests which will be reviewed and merged by the author.

