import os

def application(environ, start_response):

    code = "200 OK"
    headers = [ ('Content-type', 'text/plain') ]

    try:
        output = os.environ['PATH']

    except Exception as e:

        code = "500 Internal Server Error"
        output = str(format(e))

    start_response(code, headers)
    return [ output.encode('utf-8') ]
