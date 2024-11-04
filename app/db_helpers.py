import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("story.db")

c = db.cursor() #facilitate db ops
c.execute("PRAGMA foreign_keys = ON") #enable foreign keys for the database

users = "CREATE TABLE users(email TEXT, pwd TEXT)" 
c.execute(users)

# adds user to the database
def add_user(username, password):
    username = str(username)
    password = str(password)
    c.execute(f"INSERT INTO users(username, password) VALUES ({username}, {password})")
    c.execute("SELECT * FROM users")
    print(c.fetchall())
    c.commit()
# adds new story to the database
def add_story(title, content, user_id):
    c.execute(f"INSERT INTO stories(title, content, user_id) VALUES ({str(title)}, {str(content)}, {int(user_id)})")
    c.commit()
# adds new contribution to the database
def add_contribution(story_id, content, user_id):
    c.execute(f"INSERT INTO contributions(story_id, content, user_id) VALUES ({int(story_id)}, {str(content)}, {int(user_id)})")
    c.commit()
# returns a tuple containing the title and content of a story using story_id as an identifier 
def get_story(story_id):
    c.execute(f"SELECT title, content FROM stories WHERE story_id = {story_id}")
    story = c.fetchall()
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

c.close()