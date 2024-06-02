from flask import Blueprint

def getNewRoute(name):
    return Blueprint(name,__name__,url_prefix='/'+name)

def check():
    return "Welcome to the IPL Analyser.\n\n We have data from IPL 2008 to IPL 2023."

routes = Blueprint("base", __name__, url_prefix='/')

routes.add_url_rule('/', view_func=check)