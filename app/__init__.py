from flask import Flask, render_template, request, session #this one stores like everything
import os
import tiny, db_helpers
app = Flask(__name__)
app.secret_key =":kEA*9QiRS*k09x6t+Q|pk<"



@app.route("/register", methods=['POST', 'GET'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if db_helpers.check_username(username):
        return render_template("error.html", error = "Error: Username Already Exsists")
    else:
        db_helpers.add_user(username, password)
        user_id = db_helpers.get_user_id(username)
        # print(f"Added User: {username}")
        session['username'] = username
        session['password'] = password
        session['user_id'] = user_id
    # print(username)
    return render_template('homepage.html', user = username, all_stories = db_helpers.user_stories(user_id))
@app.route("/edited_story",  methods=['POST', 'GET'])
def edited_story():
    story_title = request.form.get('story_title')
    print(story_title)
    contribution = request.form.get('contribution')
    story_id = db_helpers.get_story_id(story_title)
    db_helpers.add_contribution(story_id[0], contribution, session["user_id"])
    return render_template('homepage.html', user = session["username"], all_stories = db_helpers.user_stories(session["user_id"]))
@app.route("/edit_story",  methods=['POST', 'GET'])
def edit_story():
    # print("dwiodhwoidhwodi")
    # print(db_helpers.open_stories(session["user_id"]))
    # print("ewfjdwdpfojkfopewjfeopwjefopj")
    return render_template('edit_story.html', user = session["username"], stories = db_helpers.open_stories(session["user_id"]))
@app.route("/create_story",  methods=['POST', 'GET'])
def create_story():
    title = request.form.get('title')
    content = request.form.get('content')
    db_helpers.add_story(title, content, session["user_id"])
    return render_template('homepage.html', user = session["username"], all_stories = db_helpers.user_stories(session["user_id"]))
@app.route("/",  methods=['POST', 'GET'])
def home():
    if 'username' and 'password' in session:
        username = session['username']
        user_id = session['user_id']
        # pwd = session['password']
        # db_helpers.add_user(user, pwd)
        # print(user)
        return render_template('homepage.html', user = user, all_stories = db_helpers.user_stories(user_id))
    return render_template( 'register.html' )

@app.route("/check_login", methods=['POST', 'GET'])
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if db_helpers.correct_login(username, password):
        session['username'] = username
        session['password'] = password
        session['user_id'] = db_helpers.get_user_id(username)
        return render_template('homepage.html', user = username, all_stories = db_helpers.user_stories(db_helpers.get_user_id(username)))
    else:
        return render_template("error.html", error = "Error: Invalid Login")
@app.route("/login",  methods=['POST', 'GET'])
def disp_loginpage():
    return render_template( 'login.html' ) 

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
