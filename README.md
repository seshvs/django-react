                                                      README 
                                                  =================
                                                  Please read the README.doc 
Installation 
----------------
1)	Clone the code `git clone <>`
2)	Create virtual env 
    a.	`cd django-react`
    b.	`mkvirtualenv django-react`
    c.	`pip install -r requirements.txt`
3)	`cd backend`
4)	start django server `./manage.py runserver` => This will start the django server at 8000 port (Note if you start the server in any other port, Then please update the frontend and django settings files).  

Now lets start Frontend.
5)	Pick another terminal  
6)	`cd django-react/frontend`
7)	`yarn install` 
8)	`yarn start `

Browser will open with a select box … 
Select Air Conditioners to fetch the details .

Select other category to find other details.


Unit tests 
----------------

Python django tests are enabled. Run `./manage.py test`. This will test all test cases developed. 

 


