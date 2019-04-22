from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

def is_length():
    test_lenght = request.form('username')
    if len(test_lenght) < 3 or len(test_lenght) > 20:
        return False
    else:
        return True



@app.route("/")
def index():
    return render_template('signup.html' ,title = "Signup")




@app.route("/", methods = ['POST'])
def user_login():
    if is_length():
        return render_template('signup.html', title = "Signup", username_error = "Please enter a user name between 3-20 char long")
    else: 
        return <h1> Correct </h1>
app.run()