from flask import Flask, jsonify

from db import WorkLogDatabase


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(test_config)
    db = WorkLogDatabase()

    @app.route('/')
    def hello():
        return jsonify({"message": "Hello world"}), 200

    @app.route('/report')
    def get_report():
        logs = db.get_all()
        report = [log.__dict__ for log in logs]
        return jsonify(report), 200

    return app
