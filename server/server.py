from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo
from userAuth import User

app = Flask(__name__)
app.secret_key = 'mysecret'

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.user_login_system

def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap


@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

#Router for members
@app.route("/members")
def members():
    return {"members": ["1", "2", "3"]} #returns JSON array

if __name__ == "__main__":
    app.run(debug=True) #start the app