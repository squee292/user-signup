from flask import Flask, request, redirect, render_template
import cgi
import os










@app.route("/")
def index():
    return render_template('signup.html' title = "Signup")
