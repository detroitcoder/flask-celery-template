from flaskapp import app
from flask import request, jsonify
import os, sys

# Add the celeryapp to the path so it can be imported (fast & dirty)
p = os.path.dirname(os.path.realpath(__file__))
np = p[:p.find(r"\flaskapp")]
sys.path.append(np)

import celeryapp.tasks as tasks

@app.route('/')
def index():
    return "flask is running"

@app.route('/add_nums', methods=["GET"])
def extract_data():
    """Accept two url paramaters, x and y and pass these to the add_numbers
    task in celery. Then return the task_id that is unique to this task so
    the result can be accessed with the /get_additions/<task_id> api"""

    x, y = request.args.get("x"), request.args.get("y")
    r = tasks.add_numbers.delay(x, y)
    return jsonify({"pid" : r.task_id})

@app.route("/get_additions/<task_id>")
def get_additions(task_id):

    result = tasks.add_numbers.AsyncResult(task_id).get(timeout=1.0)
    return jsonify({"result": str(result)})


