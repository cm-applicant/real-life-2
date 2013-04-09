# CloudMade Engineering Application

This application can be viewed in the Cloud9 IDE.

## Running

To run this code, you can log in to the Cloud9 IDE and run the django
development server. The project is located at:

    https://c9.io/cm-applicant/real-life-2
  
Once logged in, you can activate a terminal and run the django development
server to view the application.

First, activate the virtual environment:

    . env/bin/activate
    
Second, start the django development server

    cd real_life
    ./manage.py runserver $IP:$PORT
    
The magic $IP and $PORT settings are set up by Cloud9 to map all requests to
the application URL to the development server. The application is now live
at:

    http://real-life-2.cm-applicant.c9.io/

## What this application does:

The application has three roles:

  * admin
  * author
  * editor

In the `admin` role, you can edit any of the user permissions, tweet objects,
and site information about the installed application. The URL for administration
is:

    http://real-life-2.cm-applicant.c9.io/admin/
    
In the `author` role, you can log into the user-application (not the admin),
and compose tweets. Tweets will be branded and filtered based on special 
keywords, defined as regular expressions in the settings.py file. You can access
this user-application by clicking on the 'Login' link at:

    http://real-life-2.cm-applicant.c9.io/
    
In the `editor` role, you can view all the tweets that have been blocked or
flagged by inappropriate tweeting by authors. The inappropriate tweets are
listed on the first page, and editors have the option of viewing the full tweet
detail by clicking on the 'moderate' button.

## What this application doesn't do:

This application does not yet allow moderating of tweets.

## Thank you.

... and enjoy.

Please contact me for further discussion: david.zwarg@gmail.com
