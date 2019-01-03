An application where local non-profits and restaurants meet.

With Good Samaritan, businesses and food pantries can easily coordinate donation management and pick-up times.

As a local business or restaurant, you can upload items onto our inventory management system so others can view what's available.
Post your business name, phone number, and hours of operation so food pantries will be able to reach out!

As a non-profit organization, you can log in to the application, and view what local business have available for pickup!
On a first-come, first-serve basis, you can reserve items for your pantry and contact the business for a good time to swing by!
===========

to run this application on your machine

clone files

open command prompt or whichever shell you are using

run:
  pip install -r requirements.txt (to download dependencies)
  manage.py flush (to delete all existing data from db that I have on there for testing)
  manage.py createsuperuser (to create admin acct)
  manage.py makemigrations (to create tables)
  manage.py migrate

  then finally, manage.py runserver

  in your browser, navigate to localhost:8000 to open page
