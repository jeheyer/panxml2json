from panxml2json import *

def application(environ, start_response):

    import json, traceback
    from urllib import parse

    response_headers = [('Cache-Control', 'no-cache')]

    try:
        request_uri = environ.get('REQUEST_URI', None)
        if not request_uri or request_uri == "":
            request_uri = environ.get('RAW_URI', '/')
        query_string = dict(parse.parse_qsl(parse.urlsplit(str(request_uri)).query))

        json_data = json.dumps(GetData(query_string), indent=2)

        response_headers.append(('Content-type', 'application/json; charset=UTF-8'))
        response_headers.append(('Content-Length', str(len(json_data))))
        start_response('200 OK', response_headers)
        return [ json_data.encode('utf-8') ]

    except:

        response_headers.append(('Content-type', 'text/plain'))
        start_response('500 Internal Server Error', response_headers)
        return [ str(traceback.format_exc()).encode('utf-8') ]
