from flask import Flask, jsonify, request
from cr2tojpg import img_conv
from function_test import whiteBalance

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if (request.method =='POST'):
        testing_info = request.get_json()
        print(testing_info)
        return jsonify({"You sent": testing_info}), 201
    else:
        return jsonify({"about": "Post fail"})

@app.route("/CR2toJpg", methods=['GET','POST'])
def CR2toJpg():
    if (request.method =='POST'):
        process_info = request.get_json()
        location = process_info["location"]
        img_conv(location)
        return jsonify({"You sent": process_info, "output location": "/Users/User/SA109/img/black_processed.jpg"}), 201
    else:
        return jsonify({"about": "No process"})

@app.route("/whiteBalance", methods=['GET','POST'])
def wb():
    if (request.method =='POST'):
        process_info = request.get_json()
        # location = process_info["location"]
        x = process_info["x"]
        y = process_info["y"]
        z = whiteBalance(x, y)
        print(process_info)
        return jsonify({"You sent": process_info, "sum": z, "output location": "/Users/User/SA109/img/black_processed.jpg"}), 201
    else:
        return jsonify({"about": "No process"})

if __name__ == '__main__':
    app.run(debug=True)