#!/usr/bin/env python3

from flask import Flask, request, jsonify, redirect, Response
from panxml2json import GetData


app = Flask(__name__)


@app.route("/")
def panxml2json():

    try:
        _ = GetData(request.args)
        return jsonify(_)
    except Exception as e:
        return Response(format(e), 500, content_type="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
