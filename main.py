from flask import Flask, request, redirect, render_template
import string
import re

app = Flask(__name__)
app.config['DEBUG'] = True

def is_length(text):
    len_check = len(text)
    if len_check < 3 or len_check > 20:
        return False
    else:
        return True

def is_same(text1, text2):
    if text1 != text2:
        return False
    else:
        return True

def validate_email(email):
    if len(email) >= 3:
        if re.search("[@.]", email) != None:
            return True
    else:    
        return False





@app.route("/")
def index():
    return render_template('signup.html' ,title = "Signup")




@app.route("/", methods=['POST'])
def user_login():

    test_username = str(request.form["username"])
    test_password1 = str(request.form["password_one"])
    test_password2 = str(request.form["password_two"])
    test_email = str(request.form["email"])
    username_error = ''
    password_error = ''
    password_error_two = ''
    email_error = ''
    username = ''
    email = ''
    error_control = 0



    if not is_length(test_username):    
        username_error = "Please enter a user name between 3-20 char long"
        username = ''
        error_control += 1
    else:
        username = test_username

    if test_username.isspace():
        username_error = "Please enter a user name with no space"
        username = ''
        error_control += 1
    else:
        username = test_username
    
    if not is_length(test_password1):
        password_error = "Please enter a password between 3-20 char long"
        error_control += 1

    if test_password1.isspace():
        password_error = "Please enter a password with no spaces"
        error_control += 1
    
    if not is_same(test_password1, test_password2):
        password_error_two = "Passwords do not match"
        error_control += 1
    
    if validate_email(test_email) == True:
        email = test_email
    else:
        email_error = "Please enter a valid email"
        error_control += 1

    


    if error_control > 0:
        return render_template('signup.html', title = 'Signup', username = username, 
        email = email , username_error = username_error, password_error = password_error,
        password_error_two = password_error_two)
    else:
        return render_template('welcome.html', title = 'Welcome')
app.run()