from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

def is_length(text):
    len_check = len(text)
    if len_check < 3 or len_check > 20:
        return False
    else:
        return True



@app.route("/")
def index():
    return render_template('signup.html' ,title = "Signup")




@app.route("/", methods=['POST'])
def user_login():

    test_length = request.form["username"]
    username_error = ''

    if not is_length(test_length):    
        username_error = "Please enter a user name between 3-20 char long"
        return render_template('signup.html', username_error = username_error)
    
app.run()