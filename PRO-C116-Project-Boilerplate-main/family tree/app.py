# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Brian" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
app = Flask(__name__)

# define the route to mother webpage
@app.route("/")


# define the route to friends webpage
def first_flask():

    return "This is my first flask program"

# add other routes, if you want

@app.route("/flask_2")
def second_flask():
    return "Python is fun!"


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
