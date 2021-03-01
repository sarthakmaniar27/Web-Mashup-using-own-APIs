"""REST Methods i have used:
1.) GET -> to retrieve data
2.) PUT -> to update existing data
3.) POST -> to store data
4.) DELETE -> to delete record

studentAPI -> 5000 port
committeeAPI -> 5002 port
clientAPI -> 5001 port
"""

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('stud_data.json') as f:
    studDB = json.load(f)
print(studDB)


# this method is just for checking whether route is working properly or not
@app.route("/", methods=['GET'])
def welcome():
    return "Welcome alien"


# Getting all the student data
@app.route("/student/getStudents", methods=['GET'])
def getStudents():
    return jsonify({"stud": studDB})


# Fetching student details by name
@app.route("/student/getStudentDetails/<Name>", methods=['GET'])
def getStudentDetails(Name):
    student = [stud for stud in studDB if (stud["First Name"] == Name)]
    print(student)
    # print(student[0]["Email ID"])
    print(type(student))
    return jsonify({"stud": student})


# Fetching student details by UID
@app.route("/student/getStudentDetailsByUID/<UID>", methods=['GET'])
def getStudentDetailsByUID(UID):
    student = [stud for stud in studDB if (stud["UID"] == UID)]
    print(student)
    # print(student[0]["Email ID"])
    print(type(student))
    return jsonify({"stud": student})


#  updating student details
@app.route("/student/updateStudentDetails/<UID>", methods=['PUT'])
def updateStudentDetails(UID):
    student = [stud for stud in studDB if (stud["UID"] == UID)]
    print(student)
    print(student[0]["First Name"])
    if 'UID' in request.json:  # check whether this UID is there in the student data or not
        print("Student Available")
    if 'First Name' in request.json:
        student[0]['First Name'] = request.json['First Name']
    if 'Last Name' in request.json:
        student[0]['Last Name'] = request.json['Last Name']
    if 'Email ID' in request.json:
        student[0]['Email ID'] = request.json['Email ID']
    if 'Committee' in request.json:
        student[0]['Committee'] = request.json['Committee']
    return jsonify({"stud": student[0]})


#  adding student details
@app.route("/student/addStudent", methods=['POST'])
def addStudent():
    student = {
        "UID": request.json["UID"],
        "First Name": request.json["First Name"],
        "Last Name": request.json["Last Name"],
        "Email ID": request.json["Email ID"],
        "Committee": request.json["Committee"],
    }
    studDB.append(student)
    return jsonify({"stud": studDB})


#  deleting student details
@app.route("/student/removeStudent/<UID>", methods=['DELETE'])
def removeStudent(UID):
    student = [stud for stud in studDB if (stud['UID'] == UID)]
    if len(student) > 0:
        studDB.remove(student[0])
    return jsonify({"stud": student})


@app.route("/student/countStudents", methods=['GET'])
def countStudents():
    c = len(studDB)
    return "Total records in student data is " + str(c)


if __name__ == "__main__":
    app.run()

