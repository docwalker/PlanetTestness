# PlanetTestness
And now you know the REST of the story

This project was tested with 3.8.5 though likely works with earlier versions of python, 3.6 is pretty solid.

This comes delivered with all things needed to run a django test server, not meant for production.

# Setup

create a virtual environement so we don't squash anything; and install all the dependencies we'll need

` python3 -m venv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt`

Django and its dependencies should be installed, and everything should run within this virtual enviornment.

# Django bookkeeping

Before we get to running the server we need to ensure that the database is intialized

`cd restserver`

`python3 manage.py makemigrations`

`python3 manage.py migrate --run-syncdb`

you can check the options for running the web server with:

`python3 manage.py runserver --help`

 though the main option to look out for is changing bidning address and port number which can be changed by:
 
 `python3 manage.py runserver <ip>:<port>`
 
 Once running the endpoints can be reached at http://ip:port/users/ and http://ip:port/groups/
 
 # Assumptions and comments:
There was no specification for what the request for PUT /groups/ should be named for the list of users.  We made the assumption that this should be called "users" and be a list of userids.  
  
Most of the logic for handling requests were in the views classes.  After some searching and breaking a few things, it was clear that this logic should be in the serializers class.  Though it did make keeping the explicit logic of the REST functions all in one place a little easier to keep track of.
 
Testing was largely done through the django rest framework provided GUI that provides all the REST operations at the endpoints.  Some implementation details were used to handle navigating to these endpoints for other REST operations.  For example, GET /usrs/ wasn't part of the exercise but the page was the jumping off point for creating users. The endpoint expected a userid, so we coded a default value of None was a success but wtih a message that no user was created.  A list of users would have been better for visual verification.

Updates via PUT methods will blast away the User to Group associations.  It is up to the user to keep track of this when submitting UPDATES via PUT.
