from flask import Flask,Blueprint, render_template,g,request,json,jsonify
import sqlite3

# create Blueprint class with name importname Blueprintfolders
Homepage = Blueprint('homepage',__name__,url_prefix="/<url_user_id>",template_folder='',static_folder='')

#still figuring it
@Homepage.url_value_preprocessor
def user_id(endpoint,url_user_id):
    # from what i test url_user_id is a dictionary containing 'url_user_id' key with id value
    print url_user_id['url_user_id']
    g.id = url_user_id['url_user_id']

#Homepage route
@Homepage.route('/Home')
def Home(url_user_id):
    return render_template("template.html")

#see current subject route
@Homepage.route('/Subject')
def CurrentSubject(url_user_id):
    return "boo"

@Homepage.route('/Work')
def CurrentWork(url_user_id):
    return "boo"

@Homepage.route('/Score')
def CurrentScore(url_user_id):
    return "boo"