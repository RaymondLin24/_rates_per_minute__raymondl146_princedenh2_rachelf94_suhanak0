from flask import Flask, render_template, request, session #this one stores like verything
import os
import tiny
import db_helpers
app = Flask(__name__)
app.secret_key = tiny.make()

@app.route("/",  methods=['GET','POST'])
def disp_loginpage():
    if 'email' and 'password' in session:
        user = session['email']
        return render_template('login.html', name = user)
    return render_template( 'register.html' )


@app.route("/auth", methods=['POST'])
def post():
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    user = session['email']
    return render_template('homepage.html', name = user)

@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    session.pop('email', None)
    session.pop('password', None)
    return render_template('logout.html')

@app.route("/homepage", methods = ['GET', 'POST'])
def redirect():
    return render_template('homepage.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
