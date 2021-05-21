from flask import request
from json import loads
from src import app
from src.services.format_response import format_success, format_error

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return format_success()

@app.route('/error', methods=['GET'])
def error():
    # this is how you can send an error back to the caller
    return format_error(500, "Some error message"), 500

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == "GET":
        return example_get(params = request.args)
    elif request.method == "POST":
        return example_post(params = request.args, body = loads(request.data))
    else:
        return format_error(404, "Route not found"), 404

# handle GET request on /example route
def example_get(params):
    # params is a python dictionary which you can access, e.g. params["some_key_name"]
    print(params)

    return format_success(params)

# handle POST request on /example route
def example_post(params, body):
    # body is now a python dictionary which you can access, e.g. body["some_key_name"]
    print(body)

    return format_success(body)