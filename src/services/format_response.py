from flask import jsonify

def format_success(payload = {}):
    return jsonify({
        "code": 200,
        "message": "SUCCESS",
        "data": payload
    })

def format_error(code = 500, message = "", error = {}, ):
    return jsonify({
        "code": code,
        "message": message if len(message) > 0 else "ERROR",
        "error": error
    })