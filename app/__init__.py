from flask import Flask, render_template, request, session, redirect, url_of #this one stores like everything
import os
import tiny
from database import test_populate, add_user, check_username, add_story, add_contribution, get_story, contributed_to_story, correct_login, get_user_id
app = Flask(__name__)
app.secret_key = tiny.make()

@app.route("/homepage", methods = ['GET', 'POST'])
def redirect():
    session['username'] = request.form['username']
    session['password'] = request.form['password']
    user = session['email']
    return render_template('homepage.html', name = user)


@app.route("/",  methods=['GET', 'POST'])
def register():
<<<<<<< HEAD
    if 'username' and 'password' in session:
        user = session['username']
        return render_template('homepage.html', name = user)
=======
    if 'email' and 'password' in session:
        name = session['email']
        return render_template('homepage.html', user=name)
>>>>>>> 29f64a583dc8423dee1ff6a8d9053989b7ab8ed9
    return render_template( 'register.html' )


@app.route("/login",  methods=['GET','POST'])
def disp_loginpage():
<<<<<<< HEAD
    if 'username' and 'password' in session:
        user = session['username']
        return render_template('homepage.html', name = user)
=======
    if 'email' and 'password' in session:
        name = session['email']
        return render_template('homepage.html', user=name)
>>>>>>> 29f64a583dc8423dee1ff6a8d9053989b7ab8ed9
    return render_template( 'login.html' ) #renders homepage


@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return render_template('logout.html')


<<<<<<< HEAD
=======
@app.route("/homepage", methods = ['GET', 'POST'])
def redirect():
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    name = session['email']
    return render_template('homepage.html', user=name)


>>>>>>> 29f64a583dc8423dee1ff6a8d9053989b7ab8ed9
if __name__ == "__main__":
    app.debug = True
    app.run()
