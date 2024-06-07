
"""

Djengo:
======

==> Djengo is a higher leval python based framework

==> using of djengo we can build any kind of web application which is based on python

==> djengo framework written in python programing language

==> djengo is more advance and more secure

==> using of djengo we can build application rapidly


Flask: 
=====

==> flask is a python web framework 

==> using of flask we can create small leval web application


"""

"""

virtualenv - 

this is for project outside the field 
to install virtualenv we need to fire
below command

==> pip = python index package

==> to create virtualenv



step 1. ==> pip install virtualenv

step 2. ==> python -m virtualenv -p python <envname>

step 3. ==> cd <envname>

step 4. ==> Scripts\activate

step 5. ==> pip install django

step 6. ==> django-admin startproject <projectname>

step 7. ==> cd <projectname>

step 8. ==> python manage.py startapp <appname>

step 9. ==> python manage.py runserver


"""

"""

==>myproject
    ==> myfristproject
             ==>myapp
             ==>myfristproject
                 ==>setting.py

setting.py:
==========

==> main configuration file of the project

==> which is contain all the registration of the project

==> e.g.. database location
             css,js location,app 



"""


"""
cd <foldername>

cd myenv

Scripts\activate

cd myproject

python manage.py runserver

"""
"""
if we apply any in database

at that time two commands need to execute

1) python manage.py makemigrations
 ==> if will creare db script

2) python manage.py migrate
 ==> execute that script 
""" 

"""
==> createsuperuser
    ===============

1. python manage.py createsuperuser
2. admin
3. email address=admin@gmail.com
4. password
5. y    


"""
"""
vs code project stated
== ==== ======= ======

1. project   
      setting.py
          ==> INSTALLED_APPS add in <appname>
2. project
      urls.py
          ==> import include
          ==> add path 
3. app
      add urls.py
          ==> import view
          ==> add path
4. app          
      view.py
          ==> import render
          ==> create function
5. app
      create folder templates 
          create folder <appname>
              ==> create html file
              

"""