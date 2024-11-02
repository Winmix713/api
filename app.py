# Python 3.12.5

from flask import Flask, jsonify

import json

app = Flask(__name__)


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


file_path = r'C:\Users\takos\Downloads\apisajat\pythonProject2\.venv\combined_matches.json'
data = read_json_file(file_path)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to the API. Navigate to '/api/data' to get the data."


@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
