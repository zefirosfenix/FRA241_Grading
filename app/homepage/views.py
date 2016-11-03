from flask import Flask,Blueprint, render_template

# create Blueprint class with name importname Blueprintfolders
Homepage = Blueprint('homepage',__name__,template_folder='',static_folder='')

#still figuring it
#@Homepage.url_value_preprocessor
#def user_id(endpoint,id):
#    pass

#Homepage_ waiting for template
@Homepage.route('/Home')
def Home():
    return "hah"