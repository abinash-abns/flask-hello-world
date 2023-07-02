from flask import Flask,request, make_response
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "GET":
        response = make_response({"status":"200 OK"}, 200)
        return response
    elif request.method == "POST":
        response = make_response({"status":"200 POST OK"}, 200)
        return response
