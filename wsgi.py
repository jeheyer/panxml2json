#!/usr/bin/env python3

from flask import Flask, request, jsonify, render_template, Response
from panxml2json import GetData
import traceback


app = Flask(__name__)

@app.route("/vpnusermap.html")
def vpnusermap():
    return render_template('vpnusermap.html')

@app.route("/panxml2json")
def panxml2json():

    try:
        _ = GetData(request.args)
        return jsonify(_)
    except Exception as e:
        return Response(format(e), 500, content_type="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
