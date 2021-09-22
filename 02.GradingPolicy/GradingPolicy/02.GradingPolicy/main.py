from flask import Flask, request
from flask_restful import Api, Resource
from gradecalculator import calculate_mid, calculate_gpa
from helper import to_json
from helper import is_none

app = Flask(__name__)
api = Api(app)

@app.route('/midsemester/grade/<score>')
def midsemester_resource(score):
    return calculate_mid(score)

@app.route('/gpa/grade/<score>')
def gpa_resource(score, code = 'S001'):
    score = float(score)
    status = to_json( calculate_gpa(score, code) )
    return {"scoredEntered":score, "status":status}

@app.route('/gpa')
def get_gpa():
    score = request.args.get("score")
    code = request.args.get("code")
    code = is_none(code, 'S001')
    print({"code": code, "score": score})
    return gpa_resource(score, code)

if __name__ == "__main__":
    app.run(debug = True, port = 5215)