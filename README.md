# moveeasy
Problem statement:
Design a system in Django Rest Framework and AngularJS for booking a moving company which
supports the below use cases:
1. When a user starts typing an address the relevant list of addresses start auto populating in the
dropdown (Use Google API for this feature)
2. When a user selects and address and proceeds the list of relevant moving companies that are
within 50 miles of the address are displayed
3. When a user selects a moving company their calendar is displayed with availability
4. A user can select only available time slots for that company
5. On successfully selecting a moving company an email is sent to the user letting them know
about the date and time that they have selected
Attached are 3 screenshots for your reference to guide you through the process – UI does not need to
match the screenshots below – a basic UI will work

# project design and explanation
    1. we have three tables Company, Slot and BookedSlot.
    2. I am using Django user for company owner as well as end user.
    (we may have separate tables for company owner and end user for different information).
    3. Customer can request a shift any time.
        a. here client would post user_id on trip api to create a trip in waiting status
        b. In real scenario client would post source and destination for trip with user credentials
    4. Driver can select from waiting trips to make a ride.
        client patch {"status": "ongoing"} on api/v1/trip/{waiting_trip_id}/
        # in backend we check if calling user is available,
            we put a lock on trip row to update,
            change the status to ongoing and assign driver and car to trip.
    5. on operations dashboard user can refresh and get the trips with its status and timing
# stacks used
django, djangorestframework, postgresql, postgis

# pre-requisite: install postgresql with postgis extension

# project setup
1. git clone https://github.com/pk026/moveez.git
2. create a virtualenv using: virtualenv venv (install virtualenv on your machine if not already installed)
3. activate environment using: source venv/bin/activate
4. upgrade pip using: pip install --upgrade pip
5. curl https://bootstrap.pypa.io/get-pip.py | python
6. install requirements using: pip install -r requirements.txt
7. make database setting proper: create a database with name:moveez, user:pramod, password:''
or you can create database with your own set of parameters and update them into settings.py: DATABASES
8. create database schema using: python manage.py migrate
9. create a superuser: python manage.py createsuperuser
10. run: python manage.py runserver

# testbench
# request a ride
API: api/v1/trip/
Method:POST
data: {"user": 1}
(after we implement authentication we post location to server user_id we may get from auth token)

# pick the ride
API: api/v1/trip/1/?user_id=1
Method:PATCH
data: {"status": "ongoing"}
user_id in query params 
(when we implement login we can get user with auth token no need to pass this in query params)

# Customer app
put customer id if field and click ride now.
this would post: {"user": 1} on api/v1/trip/ this would create a trip with status waiting

# driver app
when driver opens up dashboard
(we identify driver by user_id query params, one we implement authentication
we can identify driver by his auth token or session token)
it calls the api: api/v1/trip/?source_app=DRIVER_APP&user_id=1

we get response like below:

