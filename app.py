# Import dependency
from flask import Flask

# Create a new flask app instance
app = Flask(__name__)

# Determine starting point of the route
@app.route('/')
def hello_world():
    return 'Hello world'