from datetime import datetime

from flask import Flask, jsonify

from app.settings import API_URL_PREFIX
from app.api.view import api as api_blueprint


app = Flask(__name__)


app.register_blueprint(api_blueprint, url_prefix=API_URL_PREFIX)


@app.route("/health-check", methods=["GET"])
def health_check():
    return jsonify({"status": "alive", "datetime": datetime.now()})


if __name__ == '__main__':
    app.run(port=5001)
