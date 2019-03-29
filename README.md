
# Readme #

## Installation ##

*	Clone the code `git clone <>`
*	Create virtual env 
    >	`cd django-react`
    >	`mkvirtualenv django-react`
    >	`pip install -r requirements.txt`
*	`cd backend`
*	start django server `./manage.py runserver` => This will start the django server at 8000 port (Note if you start the server in any other port, Then please update the frontend and django settings files).  

Now lets start Frontend.
*	Pick another terminal  
*	`cd django-react/frontend`
*	`yarn install` 
*	`yarn start `

Browser will open with a select box … 
Select Air Conditioners to fetch the details .

![image](https://user-images.githubusercontent.com/25874433/55227378-7508cc80-526b-11e9-8760-682bd7aeef69.png)


Select other category to find other details.


## Unit tests ##


Python django tests are enabled. Run `./manage.py test`. This will test all test cases developed. 

 ![image](https://user-images.githubusercontent.com/25874433/55227485-b26d5a00-526b-11e9-806a-9ae2462cc2c2.png)



