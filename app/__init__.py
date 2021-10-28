from flask import Flask, jsonify


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(test_config)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return jsonify({"message": "Hello world"}), 200

    return app
