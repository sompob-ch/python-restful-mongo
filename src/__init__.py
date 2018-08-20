from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/account", methods=["GET"])
def GetAllAccount():
    return jsonify({"about": "Hello World."})


@app.route("/account", methods=["POST"])
def CreateAccount():
    some_json = request.get_json()
    return jsonify({"you sent": some_json}), 201


def main():
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    print('deepcut connector listen on port 5000')
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()

    # app.run(host='0.0.0.0', port=data['server']['port'])
