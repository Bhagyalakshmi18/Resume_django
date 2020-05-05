# Resume Ease

Building a web application that is designed for hiring managers using Django

__Django:__ Django has been used in developing the application. Django is a Python based Framwork utilized in creating a fully developed web-application that incorporates front-end just as back-end. Front-end uses HTML, CSS, Bootstrap and JavaScript. Django bolsters Jinja templates. Django can also create dynamic web-applications and REST API which can be devoured by any customer side applications such as web-application, iOS or android application. So essentially REST API is utilized in regular backend or business rationale to each customer side application.

__Prerequisite Installations:__

    pip install django
    
__Activities Performed__

1.	For this project we had decided to develop the application using Django framework of Python.
2.	A basic home page is created that displays a brief note of how this application works 
3.	Registration form page for creating a new user is developed 
4.	The model of logging in and logging out of user profile has been developed
5.	User profile has been created where one can change display picture, update email address
6.	Challenge: A page to upload multiple resumes
Solution: Usually Django with model and forms python files, it is very difficult to upload multiple selection of files. Created widgets method with multiple attribute near forms.py file and imported in views.py file. Worked in taking any number of files
7.	The uploaded resumes are stored in local database folder created as ‘media’ in db.sqlite3
8.	After uploading the resumes the keywords.csv file is to be uploaded
9.	The model is then integrated in the backend to scripts folder. A graph is displayed on the screen and an image is automatically stored in the local folder

The only command to run the project is:

    python manage.py runserver

### Preview of Application

![Home Page](https://github.com/Bhagyalakshmi18/Resume_django/blob/master/images/Home%20page.png)


![Top 10 Candidates](https://github.com/Bhagyalakshmi18/Resume_django/blob/master/images/Top%2010%20candidates.png)
