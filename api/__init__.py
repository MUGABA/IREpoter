from flask import Flask 

app = Flask(__name__)


from api.Users.views import userblueprint
from api.Incidents.views import incidentbluerprint

app.register_blueprint(Users.views.userblueprint, url_prefix = '/v1/api/')
app.register_blueprint(Incidents.views.incidentbluerprint, url_prefix = '/v1/api/')