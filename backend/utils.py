from http import HTTPStatus
from typing import Optional


def make_response(path, body, status: Optional[HTTPStatus] = HTTPStatus.OK):
    body_len = len(body)
    status_code, status_code_msg, _ = status
    return f'HTTP/1.1 {path} {status_code} {status_code_msg}\r\nContent-Type: application/json"\r\nAccept: application/json\r\nConnection: close\r\nAccess-Control-Allow-Origin: *\r\nAccess-Control-Allow-Methods: *\r\nContent-Length: {body_len}\r\n\r\n{body}'
