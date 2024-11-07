from flask import Flask, render_template, request, session #this one stores like everything
import os
import tiny, db_helpers
app = Flask(__name__)
app.secret_key ="SECRET"

@app.route("/register", methods=['POST', 'GET'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if db_helpers.check_username(username):
        return render_template("error.html", error = "Error: Username Already Exsists")
    else:
        db_helpers.add_user(username, password)
        print(f"Added User: {username}")
        session['username'] = username
        session['password'] = password
    print(username)
    return render_template('homepage.html', user = username, all_stories = db_helpers.all_stories())

@app.route("/",  methods=['POST', 'GET'])
def home():
    if 'username' and 'password' in session:
        user = session['username']
        # pwd = session['password']
        # db_helpers.add_user(user, pwd)
        print(user)
        return render_template('homepage.html', user = user, all_stories = db_helpers.all_stories())
    return render_template( 'register.html' )

@app.route("/check_login", methods=['POST', 'GET'])
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if db_helpers.correct_login(username, password):
        session['username'] = username
        session['password'] = password
        return render_template('homepage.html', user = username, all_stories = db_helpers.all_stories())
    else:
        return render_template("error.html", error = "Error: Invalid Login")
@app.route("/login",  methods=['POST', 'GET'])
def disp_loginpage():
    if 'username' and 'password' in session:
        user = session['username']
        return render_template('homepage.html', user = user)
    return render_template( 'login.html' ) #renders homepage


@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return render_template('logout.html')





# @app.route("/login",  methods=['GET','POST'])
# def disp_loginpage():
#     if 'username' and 'password' in session:
#         user = session['username']
#         return render_template('homepage.html', name = user)
#     return render_template( 'login.html' ) #renders homepage


# @app.route("/logout", methods = ['GET', 'POST'])
# def logout():
#     session.pop('username', None)
#     session.pop('password', None)
#     return render_template('logout.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
