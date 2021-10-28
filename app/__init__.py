import json

import names

from flask import Flask, request, jsonify

from db import WorkLogDatabase
from exceptions import UserIsAlreadyOccupiedException, UserIsNotOccupiedException


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(test_config)
    db = WorkLogDatabase()

    @app.route('/')
    def hello():
        return jsonify({"message": "Hello world"}), 200

    @app.route('/work/start', methods=['POST'])
    def start_work():
        if request.method == "POST":
            data = json.loads(request.data)
            user = data.get("user", names.get_full_name())
            assignment = data.get("assignment",
                                  f"Sample assignment {len(set([log.assignment for log in db.get_all()]))}")

            try:
                log = db.add_log(user, assignment)
                return jsonify(log.__dict__()), 200
            except UserIsAlreadyOccupiedException as e:
                return jsonify({"error": f"{e}"}), 403

    @app.route('/work/end', methods=['POST'])
    def end_work():
        if request.method == "POST":
            data = json.loads(request.data)
            user = data.get("user")
            if user is None:
                return jsonify({"error": f"Must provide user in order to end his work"}), 400

            try:
                log = db.end_log(user)
                return jsonify({"log": log.__dict__()}), 200
            except UserIsNotOccupiedException as e:
                return jsonify({"error": f"{e}"}), 403

    @app.route('/report')
    def get_report():
        logs = db.get_all()
        report = [log.__dict__ for log in logs]
        return jsonify(report), 200

    return app
