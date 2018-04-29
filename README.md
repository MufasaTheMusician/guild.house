<img src="static/sheild-.png" width="150" height="150">

Guild Website
=======

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)



Intro
-------


You will need a familiarity with using CLI/shell and some an understanding of python virtual environments in order to make the process comprehensible. Following the exact steps below should work, but actually understanding what's going on is better.

Some basic web dev or django knowledge is strongly recommended. It only take a little while to learn the basics, but without them this project is going to seem a little bit intense to get set up.

If you're starting from scratch with Python/Django look through a tutorial first, we'd recommend on of these:

* Django Girls Tutorial (https://tutorial.djangogirls.org)
* The official "Writing your first Django app" Tutorial (https://docs.djangoproject.com)
* Tango With Django (https://tangowithdjango.com)
* The Django Book (https://djangobook.com/)

There are many resources out there.

Quickstart
--------------

Firstly, set up your local development environment:

#### 1. Make an environment for the project and get the codebase

If this is completely mysterious see Kenneth's guide here http://docs.python-guide.org/en/latest/dev/virtualenvs/

    # Windows start:
    pip install virtualenvwrapper-win

    # Linux/OSX start:
    pip install virtualenvwrapper

    mkvirtualenv guild.house
    
    # get the codebase
    git clone https://github.com/elena/guild.house.git
    # alternatively if you have your own clone of the project:
    # git clone https://github.com/<yourusername>/guild.house.git

    # enter your freshly minted project
    cd guild.house


#### 2. Ensure correct python packages are installed and ensure your environment is configured 


    # use the virtual environement
    workon guild.house

    # one-off install all the project dependencies
    pip install -r requirements.txt

We use the pattern of picking settings per environment. You will want to use the `development` settings.


    # get your settings
    cd project/settings
    
    # Linux/OSX
    ln -s development.py __init__.py
    
    # Windows
    mklink /d __init__.py development.py
    
    cd ../..


For security passwords aren't kept in the repository and will need to be added to your virtual environment. There are a few ways to do this but an easy way is as follows:

For Linux:


    # one-off basic environment setup
    echo 'export GUILD_DJANGO_SECRET_KEY='$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1) >> $VIRTUAL_ENV/bin/postactivate

For Windows (elevated Powershell window):
    
    
    #Set GUILD_DJANGO_SECRET_KEY as a machine level environment variable
    [Environment]::SetEnvironmentVariable("GUILD_DJANGO_SECRET_KEY", "secretkeygoeshere", "Machine")

#### 3. Run, run, run

At this point the project should work, test like this

    ./manage.py check
    # System check identified no issues (0 silenced).


If it's not working now, there's either some weird specialised configuration required on your type of system or you've either done something wrong, just go back and work through systematically or have a look at some basic django project deployment on your type of system. This is a simple project, it's pretty standard, so it shouldn't be difficult to get to this point.

Now to get some data in ...


    # one-off instantiate db, this needs to be done every time the data changes
    ./manage.py migrate

    # @@TODO make some data fixtures for some basic data

    # make yourself a superuser
    ./manage.py createsuperuser
    # ... Follow prompts to create user

    # run
    # this is done every time to run the dev server
    ./manage.py runserver


Go check out the website at:

http://localhost:8000/ or http://127.0.0.1:8000/

Now you've got it working, it's possible to do stuff.

Your superuser login will work at: http://localhost:8000/admin/

Looking at `config/urls.py` is one way of getting an idea of what apps are active.

Contact
----------


If you are having issues running the site, please log an issue with [Github Issues](https://github.com/elena/guild.house/issues) or [contact](mailto:web@guild.house):
  * Elena ([web@guild.house](mailto:web@guild.house))
