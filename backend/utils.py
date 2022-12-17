def make_response(path, body, status_code=200):
    body_len = len(body)
    return f'''HTTP/1.1 {path} {status_code}
Content-Type: application/json"
Accept: application/json
Connection: close
Access-Control-Allow-Origin: *
Content-Length: {body_len}

{body}
'''
