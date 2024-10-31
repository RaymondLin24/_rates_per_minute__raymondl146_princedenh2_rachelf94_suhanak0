from flask import Flask, render_template, request, session #this one stores like verything
import os
import tiny

app = Flask(__name__)
app.secret_key = tiny.make()

@app.route("/",  methods=['GET','POST'])
def disp_loginpage():
    if 'username' and 'password' in session:
        user = session['username']
        return render_template('homepage.html', name = user)
    return render_template( 'login.html' )


@app.route("/auth", methods=['POST'])
def post():
    session['username'] = request.form['username']
    session['password'] = request.form['password']
    user = session['username']
    return render_template('homepage.html', name = user)

@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return render_template('logout.html')

@app.route("/homepage", methods = ['GET', 'POST'])
def redirect():
    return render_template('login.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
