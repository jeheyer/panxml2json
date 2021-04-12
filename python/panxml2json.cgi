#!/usr/bin/env python3

from panxml2json import *

if __name__ == '__main__':

    import sys, os, traceback, json

    sys.stderr = sys.stdout

    query_fields = {}

    if os.environ.get('REQUEST_URI'):

        import cgi

        query_fields_objects = cgi.FieldStorage()
        for key in query_fields_objects:
            value = query_fields_objects[key].value
            query_fields[key] = str(value)

    response_headers = [('Cache-Control', 'no-cache')]

    try:
        json_data = json.dumps(GetData(query_fields), indent = 2)

        if os.environ.get('REQUEST_METHOD'):

            response_headers.append(('Content-Length', str(len(json_data)+1)))
            response_headers.append(('Content-Type', 'application/json; charset=UTF-8'))
            for _ in response_headers:
                print(f"{_[0]}: {_[1]}")
            print(f"\n{json_data}")
        else:
            print(data)

    except Exception as e:
        print("Status: 500")
        response_headers.append(('Content-Type', 'text/plain'))
        for _ in response_headers:
            print(f"{_[0]}: {_[1]}")
        print()
        traceback.print_exc(file=sys.stdout, limit = 3)

    sys.exit()
