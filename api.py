# this file contains the api wrapper that are used
# receive and send requests to and from the server.
import flask
from flask import request,jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# define the API route here
@app.route('/',methods=['GET'])
def home('/question'):
    return '''Something is fishy here'''