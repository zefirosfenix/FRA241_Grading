from flask import Flask,redirect,url_for
from login.views import Login

#declare flask app
Grading = Flask(__name__)

#register blueprint
Grading.register_blueprint(Login)

#default route
@Grading.route('/')
def a():
    return redirect(url_for('login.login'))

#run app
Grading.run()