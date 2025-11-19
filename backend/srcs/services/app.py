from flask import Flask, jsonify, request, abort
import sys
import os
from flask import Flask, Response
from flask_cors import CORS
from flask import Flask
from flask import jsonify



app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


app.debug = True
app.config["SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["PREFERRED_URL_SCHEME"] = "https"


@app.errorhandler(500)
def internal_server_error(e):
    print(e, file=sys.stderr)
    # note that we set the 500 status explicitly
    return "ok", 500

app.register_error_handler(500, internal_server_error)
app.register_error_handler(400, internal_server_error)

@app.before_request
def before_request():
    # headers = {
    #     'Access-Control-Allow-Origin': 'dictionnaire.kofl.ch',
    #     'Access-Control-Allow-Methods': "GET, POST, PUT, DELETE, OPTIONS",
    #     'Access-Control-Allow-Headers': "Origin, X-Requested-With, Content-Type, Accept, Authorization, authorization",
    #     "Access-Control-Allow-Credentials": "true",
    # }
    
    if request.method == 'OPTIONS' or request.method == 'options':
        return Response()
    pass
    # print(request.get_json())

@app.after_request
def add_header(response):
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Access-Control-Allow-Methods'] = 'POST,GET,PATCH,OPTIONS'
    print("responding", response.headers)
    return response

import traceback
@app.errorhandler(Exception)
def server_error(err: Exception):
    # print(traceback.format_exc(), file=sys.stderr)
    print("Error: ", err)
    if len(err.args) == 0:
        return jsonify({}), 404
    if len(err.args) > 1 and not type(err.args[0]) is dict:
        return jsonify(err.args[1]), err.args[0]
    app.logger.exception(err.args[0])
    return jsonify({}), 500

@app.route("/ping")
def ping():
    return jsonify({
        "pong": "pong",
        "ip": request.remote_addr
    })

# emit('connect', {'data': 'Connected'})