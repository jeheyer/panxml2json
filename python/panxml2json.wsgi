#!/usr/bin/env python3

from panxml2json import *

def application(environ, start_response):

    import json, traceback

    query_string = {}

    response_headers = [('Cache-Control', 'no-cache')]

    try:
        if '?' in environ['REQUEST_URI']:
            for _ in environ.get('QUERY_STRING', None).split('&'):
                [key, value] = _.split('=')
                query_string[key] = value

        json_data = json.dumps(GetData(query_string), indent=2)

        response_headers.append(('Content-type', 'application/json; charset=UTF-8')) 
        response_headers.append(('Content-Length', str(len(json_data))))
        start_response('200 OK', response_headers)
        return [ json_data.encode('utf-8') ]

    except:

        response_headers.append(('Content-type', 'text/plain')) 
        start_response('500 Internal Server Error', response_headers)

        # Return error message via traceback
        error = traceback.format_exc()
        return [ str(error).encode('utf-8') ]

