from flask import Flask,Blueprint, render_template,g,request,json,jsonify
import sqlite3

# create Blueprint class with name importname Blueprintfolders
Homepage = Blueprint('homepage',__name__,url_prefix="/<url_user_id>",template_folder='',static_folder='')

#still figuring it
@Homepage.url_value_preprocessor
def user_id(endpoint,url_user_id):
    print url_user_id
    g.id = url_user_id

#Homepage_ waiting for template
@Homepage.route('/Home')
def Home(url_user_id):
    return render_template("template.html")