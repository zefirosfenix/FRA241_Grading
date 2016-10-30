from flask import Flask,Blueprint, render_template

# create Blueprint class with name importname Blueprintfolders
Homepage = Blueprint('homepage',__name__,url_prefix='/<user_url_slug>',template_folder='',static_folder='')

@Homepage.url_value_preprocessor
def user_id(endpoint,id):
    pass

@Homepage.route('/Home')
def Home():
    return 0