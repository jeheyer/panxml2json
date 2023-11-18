#!/usr/bin/env python3

from flask import Flask, request, jsonify, render_template, Response
from panxml2json import get_data, read_settings
from traceback import format_exc

app = Flask(__name__)


@app.route("/")
def root():
    try:
        device_list = get_data({'command': "list_devices"})
        device_name = None
        commands = get_data({'command': "list_commands"})
        data = []
        if command := request.args.get('command'):
            args = {'command': command}
            if device_name := request.args.get('device_name'):
                args['device_name'] = device_name
            data = get_data(args)
        return render_template('index.html', command=command, data=data, commands=commands,
                               device_list=device_list, device_name=device_name)
    except Exception as e:
        return Response(format_exc(), 500, content_type="text/plain")


@app.route("/vpnusermap.html")
def vpnusermap():
    try:
        device_list = get_data({'command': "list_devices"})
        device_name = request.args.get('device_name')
        settings = read_settings()
        return render_template('vpnusermap.html', device_list=device_list, device_name=device_name,
                               google_maps_api_key=settings.get('google_maps_api_key'))
    except Exception as e:
        return Response(format_exc(), 500, content_type="text/plain")


@app.route("/panxml2json")
def panxml2json():

    try:
        _ = get_data(request.args)
        return jsonify(_)
    except Exception as e:
        return Response(format_exc(), 500, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
