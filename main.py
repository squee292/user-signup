from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

def is_length(text):
    len_check = len(text)
    if len_check >= 3 and len_check <= 20:
        return True
    else:
        return False



@app.route("/")
def index():
    return render_template('signup.html' ,title = "Signup")




@app.route("/validate", methods = ['POST'])
def user_login():
    
    test_lenght = request.form['username']
    username_error = ''

    if not is_length(test_length):
        username_error = "Please enter a user name between 3-20 char long"
        return render_template('signup.html', title = "Signup", username_error = username_error)
    
app.run()