from flask import Flask, request, redirect, render_template


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

def email_check(text):
    x = 0
    y = 0
    for n in text:
        if n = '@':
            x += 1
        if n = '.':
            y += 1
        if x >= 2 or y >= 2:
            return False
        else:
            return True



@app.route("/")
def index():
    return render_template('signup.html' ,title = "Signup")




@app.route("/", methods=['POST'])
def user_login():

    test_length = request.form["username"]
    test_password1 = request.form["password_one"]
    test_password2 = request.form["password_two"]
    test_email = request.form["email"]
    username_error = ''
    password_error = ''
    password_error_two = ''
    email_error = ''
    username = ''
    email = ''


    if not is_length(test_length):    
        username_error = "Please enter a user name between 3-20 char long"
        username = ''
    else:
        username = str(test_length)
    
    if not is_length(test_password1):
        password_error = "Please enter a password between"
    
    if not is_same:
        password_error_two = "Passwords do not match"
        
    
app.run()