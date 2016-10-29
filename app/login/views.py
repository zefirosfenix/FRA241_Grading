from flask import Flask,Blueprint, render_template

# create Blueprint class with name importname Blueprintfolders
Login = Blueprint('login',__name__,template_folder='templates',static_folder='app/login')

#declare url route
@Login.route('/login')
# what we do in this route
def login():
    return render_template('template.html')
