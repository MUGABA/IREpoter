from flask import Flask 

app = Flask(__name__)


from api.Users.views import userblueprint

app.register_blueprint(Users.views.userblueprint, url_prefix = '/v1/api/')