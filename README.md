# Bus Booking Application

![Image Gallery](https://www.greatbuyz.com/blog/wp-content/uploads/2017/11/booking-bus-ticket.jpg)
https://github.com/jameskomo/bus-reservation-system/blob/master/myapp/static/img/bus1.jpg

This is a Python-Django reservation system that allows passengers to search buses to book based on origin and destination, book buses and see billings, Cancel reservations with full authentication for login, register and profile managemnt

You can see the live Application here [BuuPass](https://komo-buupass.herokuapp.com/).

Author Information
========
James Komo 

Features
========

- Built with Python 3.6, Djang0 2.0 Framework
- Styled using Bootstrap4
- Uses PostgreSQL DB and Deployed to Heroku
Allows users to:
- Sign in with the application to start using.
- Set up a profile about and manage your details
- Search for buses based on source and destination
- Bookin buses 
- Cancel bus reservations
- View buses booked and cancelled
- View available buses listing

Behavior Driven Development (BDD)
================================
| Input               | Output                                                                                                                 |   |   |   |
|---------------------|------------------------------------------------------------------------------------------------------------------------|---|---|---|
| User Opens Homepage | The user is required to login or signup to access booking services but can search buses withthout authentication       |   |   |   |
| User Signs up       | A user profile is created automatically through Django Signals and they are redirected to the home page                |   |   |   |
| User Signs In       | The user is redirected to home page with various navigation options                                                    |   |   |   |
| User Click Profile  | The user is able to update their profile details and save                                                              |   |   |   |
| Find Bus            | The user is navigated to another page where they can enter search parameters                                           |   |   |   |
| Search Bus          | After clicking Search bus, the user either gets no buses available message or is redirected to available buses listing |   |   |   |
| Book Bus            | On selecting book bus, the user is asked to enter number of seats interested and the Bus ID                            |   |   |   |
| Bill Details        | After booking bus, the user is presented with their billing details including total amounts                            |   |   |   |
| Cancel Bus          | The user is asked to enter bus ID and the status changes to CANCELLED                                                  |   |   |   |
| View Bookings       | On clicking this link, the user is able to view all booking history                                                    |   |   |   |

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
### Application ScreenShots
#### Book or Cancel
https://github.com/jameskomo/bus-reservation-system/blob/master/myapp/static/img/application%20images/bookandcancel.png?raw=true

#### Bus Listing
https://github.com/jameskomo/bus-reservation-system/blob/master/myapp/static/img/application%20images/buslisting.png?raw=true

#### No Buses
https://github.com/jameskomo/bus-reservation-system/blob/master/myapp/static/img/application%20images/nobuses.png?raw=true

#### Authentication
https://github.com/jameskomo/bus-reservation-system/blob/master/myapp/static/img/application%20images/login.png?raw=true

https://github.com/jameskomo/bus-reservation-system/blob/master/myapp/static/img/application%20images/logout.png?raw=true


### Prerequisites

You will need to:

-   Have python installed
-   Have PostgreSQL DB installed
-   Have a terminal to interact with the app.
-   Any text editor
-   Browser to view
-  -Create a Virtual Environemnt, install Django >=2.0 and its dependencies


Installation
========

    $ git@github.com:jameskomo/bus-reservation-system.git


Build & Deployment
========

**NOTE:** You need to have fully cloned it to run it locally.


    (virtual) $ python3.6 manage.py runserver

    # it will launch the web page from local server. You can also visit the livelink [here](https://komo-buupass.herokuapp.com/).
 to use the system

##Built With

- Built with Python 3.6
- Django2.0
- Styled using Bootstrap

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!

Known Bugs
========
There are currently no known bugs for the app. However, I will be updating the README incase any bugs arise.

## License

MIT License

Copyright (c) 2019 James Komo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
