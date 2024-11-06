import sqlite3 #enable SQLite operations
from flask import session

#open db if exists, otherwise create
db = sqlite3.connect("story.db")
c = db.cursor() #facilitate db ops
c.execute("PRAGMA foreign_keys = ON") #enable foreign keys for the database

#populates database for testing purpouses
def test_populate():
    for i in range(0, 10):
        i = str(i)
        username = 'username ' + i
        password = 'password ' + i
        title = 'title ' + i
        content = 'content ' + i
        contribution = 'contribution ' + i
        i = int(i)
        user_id = story_id = i + 1
        add_user(username, password)
        add_story(title, content, user_id)
        add_contribution(story_id, contribution, user_id)
# adds user to the database
def add_user(username, password):
    c.execute(f"INSERT INTO users(username, password) VALUES ('{username}', '{password}')")
    db.commit()
# returns true if a username is in the users table, false otherwise
def check_username(username):
    c.execute("SELECT username FROM users")
    usernames = c.fetchall()
    for user in usernames:
        if (user == username):
            return True
    return False
# adds new story to the database
def add_story(title, content, user_id):
    c.execute(f"INSERT INTO stories(title, content, user_id) VALUES ('{str(title)}', '{str(content)}', '{int(user_id)}')")
    db.commit()
# adds new contribution to the database
def add_contribution(story_id, content, user_id):
    c.execute(f"INSERT INTO contributions(story_id, contribution, user_id) VALUES ('{int(story_id)}', '{str(content)}', '{int(user_id)}')")
    db.commit()
# returns a dictionary where 'title' is the index of hte title and 'content' is the index of hte content of the story
def get_story(story_id):
    c.execute(f"SELECT title, content FROM stories WHERE story_id = {story_id}")
    story = c.fetchall()[0]
    c.execute(f"SELECT contribution FROM contributions WHERE story_id = {story_id}")
    contributions = c.fetchall()[0]
    complete_story = {}
    complete_story["title"] = story[0]
    complete_story["content"] = story[1]
    for i in contributions:
        complete_story["content"] = complete_story["content"] + " " + i
    print(complete_story)
    return story
# returns true if a user contributed to a story, false otherwise
def contributed_to_story(user_id, story_id):
    rows = []
    c.execute(f"SELECT * FROM stories WHERE story_id = {story_id} AND user_id = {user_id}")
    rows.append(c.fetchall())
    c.execute(f"SELECT * FROM contributions WHERE user_id = {user_id} AND story_id = {story_id}")
    rows.append(c.fetchall())
    for i in rows:
        if len(i) == 0:
            return False
    return True
# returns true if giving a matching username and password in the database false otherwise
def correct_login(username, password):
    c.execute(f"SELECT * FROM users WHERE username = '{str(username)}' AND password = '{str(password)}'")
    user_info = c.fetchall()[0]
    if len(user_info) == 0:
        return False
    else:
        return True
#retrieves user_id given username
def get_user_id(username):
    c.execute(f"SELECT user_id FROM users WHERE username = '{str(username)}' ")
    return c.fetchall[0][0]
def create_tables():
    c.execute("CREATE TABLE users(user_id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)")
    c.execute("CREATE TABLE stories(story_id INTEGER PRIMARY KEY, title TEXT NOT NULL, content TEXT NOT NULL, user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users(user_id))")
    c.execute("CREATE TABLE contributions(contribution_id INTEGER PRIMARY KEY, story_id INTEGER, user_id INTEGER, contribution TEXT NOT NULL, FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (story_id) REFERENCES stories(story_id))")
correct_login('username 0', 'password 0')