import os
from flask import Flask
from src.services.format_response import format_success

app = Flask(__name__)

from src import *
from src.routers import *

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)))

@app.route('/')
def init():
    return format_success()
