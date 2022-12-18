import json
from typing import Union

from exceptions import BadRequestError


class Request:
    host: str = None
    method: str = None
    http_version: str = None
    path: str = None
    body: Union[str, dict] = ''

    def __init__(self, raw_http: str):
        first_line = raw_http[:raw_http.find('\r\n')]
        self.method, self.path, self.http_version = first_line.split()
        if self.method in ["POST", "PUT"]:
            body = raw_http[raw_http.find('\r\n\r\n') + 4:]
            self.body = body

    @property
    def json(self):
        try:
            result = json.loads(self.body)
        except json.JSONDecodeError:
            raise BadRequestError()
        return result

    def __str__(self):
        return f'<Request: {self.method}, path=({self.path})> (body_length:{len(self.body)})'

