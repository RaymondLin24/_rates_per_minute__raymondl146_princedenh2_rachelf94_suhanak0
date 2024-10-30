from flask import Flask, render_template, request, session #this one stores like verything
import os

app = Flask(__name__)

@app.route("/")
def disp_loginpage():
    print("Login Page")
    print(__name__)
    return render_template( 'login.html' )

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
