from flask import Flask, jsonify, render_template, flash, request
import json
import requests
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

with open('committee_data.json') as f:
    comDB = json.load(f)
print(type(comDB))


# @app.route("/home", methods=['GET'])
# def home():
#     k = "ECELL"
#     url1 = f"http://localhost:5002/committee/getCommitteeDetails/{k}"
#     r1 = requests.get(url1)
#     print(r1.json())
#     url2 = "http://localhost:5000/student/getStudents"
#     r2 = requests.get(url2)
#     r2 = r2.json()["stud"]
#     # print(r2.json())
#     # r2 = r2["stud"]
#     for r in r2:
#         if r["Committee"] == k:
#             print(r)
#     return render_template('result.html')


@app.route('/')
def homeOriginal():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # result = request.form
        k = request.form.get("Name")
        if len(k) == 0:
            return render_template("result.html", result=["No students in this committee found!!"], value="Empty "
                                                                                                          "input!!")
        # print(k)
        url1 = f"http://localhost:5002/committee/getCommitteeDetails/{k}"
        r1 = requests.get(url1)
        r1 = r1.json()["com"]
        # print(r1.json())
        url2 = "http://localhost:5000/student/getStudents"
        r2 = requests.get(url2)
        r2 = r2.json()["stud"]
        # print(type(r2))
        # print(r2.json())
        # r2 = r2["stud"]
        studName = []
        about = ""
        flag = 0
        for r in r1:
            if r["name"] == k:
                # print(r["about"])
                about = r["about"]
                flag = 1
            else:
                about = "Oops! No Committee Found"
                # print(about)
        for r in r2:
            if r["Committee"] == k:
                temp = r["First Name"] + " " + r["Last Name"]
                studName.append(temp)
                # print(r)
                # print()
        # print(studName) if (len(studName) > 0) else print("No students in this committee found!!")
        # print(about) if (flag == 1) else print("Oops! No Committee Found")

        if len(studName) > 0 and flag == 1:
            return render_template("result.html", result=studName, value=about)
        else:
            return render_template("result.html", result= ["No students in this committee found!!"], value="Oops! No Committee Found")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
