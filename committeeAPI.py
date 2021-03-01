from flask import Flask, jsonify
import json
import requests


app = Flask(__name__)

with open('committee_data.json') as f:
    comDB = json.load(f)
print(type(comDB))


@app.route("/committee/getCommittees", methods=['GET'])
def getCommittees():
    return jsonify({"com": comDB})


@app.route("/committee/getCommitteeDetails/<Name>", methods=['GET'])
def getCommitteeDetails(Name):
    committee = [com for com in comDB if (com["name"] == Name)]
    print(committee)
    return jsonify({"com": committee})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5002)
