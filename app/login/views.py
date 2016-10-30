from flask import Flask,Blueprint, render_template

# create Blueprint class with name importname Blueprintfolders
Login = Blueprint('login',__name__,template_folder='',static_folder='app/login')

#declare url route
@Login.route('/login')
# what we do in this route
def login():
    return render_template('login_from_w3.html')
