# Copilot help me create a python api

from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

# Help me create route to sum 2 numbers
@app.route('/sum/<int:num1>/<int:num2>', methods=['GET'])
def sum(num1, num2):
    return str(num1 + num2)
