# Random user generator
It is a RESTful API which can be called to generate truly random users details. The API use Generative Adverserial Networks(GAN) to generate truely random images each time the API is called.

## How to Install and Run the Project
1. First clone the repository: <br>
<code>git clone</code> followed by the HTTPS address of the project 
<br><br>
2. Create a python environment so that the correct package versions can be installed without affecting your default env, using:<br>
<code>pip install -r requirements.txt</code><br><br>
3. The Procfile and the wsgi.py file are for deployment and can be ignored<br><br>
4. Just run the app.py file using <code>python app.py</code> which would start the server on localhost:5000. The API can be called using localhost:5000/generate_user.<br><br>
5. The server might throw 'cudart64_110.dll not found' error if your machine doesn't have a GPU. The API should run never-the-less.
<br><br>

## Steps to Deploy on Render.com
1) First pip install gunicorn for your project so that it can be used in development.<br> 
Web applications that process incoming HTTP requests concurrently make much more efficient use 
of dyno resources than web applications that only process one request at a time. Because of this, we 
recommend using web servers that support concurrent request processing whenever developing 
and running production services.<br>
The Django and Flask web frameworks feature convenient built-in web servers, but these blocking 
servers only process a single request at a time. Gunicorn is a pure-Python HTTP server for WSGI 
applications. It allows you to run any Python application concurrently by running multiple Python 
processes within a single dyno. It provides a perfect balance of performance, flexibility, and 
configuration simplicity.<br><br>
2) Create a .py file which would be used by gunicorn to run your app. Here in “from app import app”
first app is for the app.py file which is the entry point (also named as index.py sometimes) and the 
second app is the app created in that app.py file by flask.<br><br>
![wsgi.py](https://user-images.githubusercontent.com/79781280/211367428-3de306ef-f603-4d54-903a-34fab1250091.png "wsgi.py")

3) Update your “requirement.txt” file.<br><br>
4) Push your project on github.<br><br>
5) Create an account on render.com. This can be done through your github account. This will 
automatically sync all your repositories with render.<br><br>
![image](https://user-images.githubusercontent.com/79781280/211367565-ee9f2a5b-8065-47f1-be8a-837b932a045a.png)

6) Click on “New” and select “Web Services”.<br><br>
![image](https://user-images.githubusercontent.com/79781280/211367903-e7194fd2-d523-4c59-b0bf-1851ed9d812e.png)

7) All your public repositories would be visible. Connect the repository to be deployed.<br><br>
8) Give an appropriate name, leave the region, root directory, branch (assuming you are on main
branch) and environment as it is. For build path it would be “pip install -r requirements.txt”. Start 
command would be for example, “gunicorn wsgi:app” in this case where wsgi is startup file and app 
is the name of the flask app. This is similar to command in the Procfile used in Heroku.<br><br>
9) Ensure you are using the free-tier and click on “Create Web Service”. This should start deploying 
API. Any errors regarding the version incompatibilities would be flashed in the window. Once 
deployed if you are having “Internal Server Errors” you can check the logs. If any changes are made 
to the code on github, you have the option to manually deploy the desired commit. Once deployed it 
should show you “Live” and the url would be given below the web service name.<br><br>
![image](https://user-images.githubusercontent.com/79781280/211367946-ac4bfa15-b0a8-4d39-a8db-bc4ee41ceb48.png)


