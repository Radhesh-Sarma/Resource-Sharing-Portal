# Resource Sharing website

Web portal to help people connect with each other and share resources and goods.

## Installing
1.Clone the repo and configure the virtual environment

2. Set up the initial migration build the database.

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

3.  Create a superuser:

```
$ python3 manage.py createsuperuser
```

4.  Confirm everything is working:

```
$ python3 manage.py runserver
```

## Authors

* [Radhesh Sarma](https://github.com/Radhesh-Sarma) &nbsp;&nbsp;&nbsp;
* [Simran Sahni](https://github.com/Simran-Sahni)&nbsp;&nbsp;
* [Nikhil Mohan Krishna](https://github.com/samael042)&nbsp;&nbsp;
* [Raunak Mantri](https://github.com/raunakmantri9)&nbsp;&nbsp;&nbsp;&nbsp;
* Thanks to [William](https://github.com/wsvincent) for DjangoX boilerplate and to [Pranjal Shukla](https://www.facebook.com/PataNahi0)&nbsp; for valuable feedback, suggestions
## To be added

* Change the model so that user can select the type of resource(food,books,clothes) 
* add Captcha on login,signup,adding a post
* Picture upload
* Data Science / Analysis of donation , Plotting a heat map. 
* Divide the webpage to 3 parts, One part for donation , one for Buy and Sell@BPHC,one for cab sharing
* 3 options after login or 3 parts of the webpage,one for Donate ,buy and sell , cab sharing 
* Make a seperate tab for cab sharing, if anyone books ola/uber on campus can use this page to share timings, add your departure timings , page will suggest earlist booked and empty cab.
* Different tables for non perishable items and perishable items ,one for perishable.
* For a perishable item user can select a date, time from calendar to indicate a timer
* Android / IOS App support for the same.
* Suggest a suitable good name for our website
* Add text editor functionality to description box, to allow user to edit properly ,make bulletin points
* for books , clothes user can select quantity , quality of product as in [' good state',' poor state',' just out of the box'],add reason for selling
* Add functionality for user privacy , someone may not like to share phone number , address, email to others, Website may be used as a database for criminals, as in someone can loot someone leiu of meeting to sell/buy
* User should have an option to chat anonymously, girls may not like to reveal their contact details to strangers.Their contact details may go to mess workers.
 
## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**



