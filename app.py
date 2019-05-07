#app.py

from api import API
from hello_world import hello_world

app = API()


@app.route("/home")
def home(request, response):
    response.text= "Hello from the HOME page"

@app.route("/about")
def about(request, response):
    response.text= "Hello from the ABOUT page"

@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"