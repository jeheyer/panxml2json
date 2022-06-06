#!/usr/bin/env python3

from panxml2json import *

def application(environ, start_response):

    import json, traceback
    from urllib import parse

    response_code = "200 OK"
    response_headers = [('Cache-Control', 'no-cache')]

    try:
        request_uri = environ.get('REQUEST_URI', None)
        if not request_uri or request_uri == "":
            request_uri = environ.get('RAW_URI', '/')
        query_string = dict(parse.parse_qsl(parse.urlsplit(str(request_uri)).query))

        output = json.dumps(GetData(query_string), indent=2)
        response_headers.append(('Content-type', 'application/json; charset=UTF-8'))
        response_headers.append(('Content-Length', str(len(output))))

    except:

        response_code = "500 Internal Server Error"
        response_headers.append(('Content-type', 'text/plain'))
        output = str(traceback.format_exc())    

    start_response(response_code, response_headers)
    return [ output.encode('utf-8') ]

