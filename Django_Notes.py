#Specific notes and commands for the Django Girls Project
# username: wrightaq password: Django
# create venv: python3.12 -m venv myvenv
# start venv:source myvenv/bin/activate
# to start server: python manage.py runserver
# local database is different than database on PythonAnywhere
# to exit python shell type exit()

#-------------------------------------------------------------------
#HTML Notes
# {% %} is notation for Django template tags
# <a> is used for GET requests while forms are used for POST requests

#---------------------------------------------------------------------
#General Django flow:
# -Djangos urlresolver takes url, along with request information, and matched it to an function or 'view'.
# -The View then takes the request information can do functions like look into the database, then generates a response
# that is sent back to web browser
    #general flow: add to base template, add to urls, add to view, create extending template, check locally, deploy

#-------------------------------------------------------------------------------
#Virtual Environment:
# -isolates you python/django setup on a per-project basis (I had to stop the first venv when my python update wasn't compatible with Django)
# -the commmand to make a virtualenv: $ python3 -m venv myvenv (myvenv=whatever you want to can it)
# -the command to start the env: $ source myvenv/bin/activate

#--------------------------------------------------------------------------------
#Django's interactive console, interact with the local database:
#-command to start inside venv: $ python manage.py shell
#-import models into the database (ex. from blog.models import Post)
#-create new Post object in database: Post.objects.create(author=me, title='Sample title', text='Test')
#-import User model: from django.contrib.auth.models import User
#-use exit() to leave shell

#-------------------------------------------------------------------------------------
#Updating the static files on PythonAnywhere in an active venv:
  # $ workon <your-pythonanywhere-domain>.pythonanywhere.com
  #(wrightaq.pythonanywhere.com)$ python manage.py collectstatic

#-------------------------------------------------------------------------------------
#Some things I'm unclear on:
# -migrations (used with manage.py file)