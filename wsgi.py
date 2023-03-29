#!/usr/bin/env python3

from flask import Flask, request, jsonify, render_template, Response
from panxml2json import get_data
import traceback


app = Flask(__name__)

@app.route("/vpnusermap.html")
def vpnusermap():
    try:
        device_list = get_data({'command': "list_devices"})
        return render_template('vpnusermap.html', device_list=device_list)
    except Exception as e:
        return Response(format(e), 500, content_type="text/plain")    

@app.route("/panxml2json")
def panxml2json():

    try:
        _ = get_data(request.args)
        return jsonify(_)
    except Exception as e:
        return Response(format(e), 500, content_type="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
