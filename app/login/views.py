from flask import Flask,Blueprint, render_template, jsonify, json
import sqlite3


ID = []
Password = []
# create Blueprint class with name importname Blueprintfolders
Login = Blueprint('login',__name__,template_folder='',static_folder='')

# import username and password from Data.db
conn = sqlite3.connect('Data.db') #connect Data.db
c = conn.cursor()
cursor = c.execute("SELECT ID, Password from User") #read ID and password from conn
ID = []
Password = []
for row in cursor:
     ID.append(str(row[0]))
     Password.append(str(row[1]))

#declare url route
@Login.route('/login')
# what we do in this route
def login():
    return render_template('login_from_w3.html')


@Login.route('/background_process')
def background_process():
    return jsonify(id = ID,password = Password) #send sudo json file with id & password(don't create new files)
    

