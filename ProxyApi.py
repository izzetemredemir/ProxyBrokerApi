from flask import Flask ,jsonify , request
from ProxyService import ProxyService

app = Flask(__name__)
p = ProxyService(limit=10)

@app.route("/",methods=['GET','POST'])
def index():
    return jsonify({"proxy":p.getProxy()})

@app.route("/cmd",methods=['GET','POST'])
def cmd():
    if (request.method == "POST"):
        pjson = request.get_json()
        if(pjson["clear"]=="used_proxies"):
            p.clear_used_proxies()
            return jsonify({"json": pjson}), 201
        elif (pjson["clear"] == "proxies"):
            p.clear_proxies()
            return jsonify({"json": pjson}), 201

        elif (pjson["clear"] == "all"):
            p.clear_all()
            return jsonify({"json": pjson}), 201
        else:
            return jsonify({"json": "FalseCommand"}), 201

    else:
        return jsonify({"json": "FalseRequest"}), 201


if __name__ == "__main__":
    p.getProxy()
    app.run(debug=True)
