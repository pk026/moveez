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
        a. user will seeach for the address and picks on from the suggestion
        b. when user selects address angular does ajax request to django server with lattitide and longitue on selected address.
        c. Django sever filter the companies which are within the 50Km of selected point and returns Json on list of companies.
        d. Angular then renders the list of companies.
        e. When user clicks on company angular calls slot API with company id
        f. Slot API returns future slot which user can select and confirm for booking.
        g. On confirm booking angular does patch request to book than slot
        h. backend saves the booking and fires a email to user of confirmation.

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


#APIs request response
http://localhost:8000/api/v1/company/?lat=18.9695&lng=72.8193
[
    {
        "id": 4,
        "name": "test",
        "address": null,
        "latitude": 18.9695,
        "longitude": 72.8193,
        "position": "SRID=4326;POINT (18.9695 72.8193)",
        "is_deleted": false,
        "created": "2018-11-13T17:45:13.367524Z",
        "updated": "2018-11-13T17:45:13.367571Z",
        "owner": 1
    }
]
i/v1/slot/?company_id=1
[
    {
        "id": 1,
        "date": "2018-11-15",
        "time": "01:00:00",
        "availability": true,
        "is_deleted": false,
        "created": "2018-11-13T17:53:51.454361Z",
        "updated": "2018-11-13T17:53:51.454404Z",
        "company": 1
    },
    {
        "id": 2,
        "date": "2018-11-15",
        "time": "02:00:00",
        "availability": true,
        "is_deleted": false,
        "created": "2018-11-13T17:53:55.597522Z",
        "updated": "2018-11-13T17:53:55.597565Z",
        "company": 1
    },
    {
        "id": 3,
        "date": "2018-11-15",
        "time": "03:00:00",
        "availability": true,
        "is_deleted": false,
        "created": "2018-11-13T17:53:59.032354Z",
        "updated": "2018-11-13T17:53:59.032394Z",
        "company": 1
    },
    {
        "id": 4,
        "date": "2018-11-15",
        "time": "04:00:00",
        "availability": true,
        "is_deleted": false,
        "created": "2018-11-13T17:54:01.840674Z",
        "updated": "2018-11-13T17:54:01.840713Z",
        "company": 1
    },
    {
        "id": 5,
        "date": "2018-11-15",
        "time": "05:00:00",
        "availability": true,
        "is_deleted": false,
        "created": "2018-11-13T17:54:05.030183Z",
        "updated": "2018-11-13T17:54:05.030222Z",
        "company": 1
    }
]
