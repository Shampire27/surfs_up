# 1. import Flask
from flask import Flask

# 2. Create am app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user goes to the index route
@app.route('/')
def hello_world():
    return 'Hello world'

# 4. Run a Flask App (in TERMINAL):
# conda activate PythonData
# for Mac, run in command lines: export FLASK_APP=app.py
# for Windows system run: set FLASK_APP=app.py
# then: flask run
