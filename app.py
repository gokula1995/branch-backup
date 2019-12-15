from flask import Flask, request, jsonify, json
from biz.getRepoDetails import validate_repo_info


app = Flask(__name__)
@app.route('/', methods=["POST"])
def github_payload():
    data = request.get_json()
    repo_data = validate_repo_info(data)
    return repo_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8990)
