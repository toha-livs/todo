from asyncio import StreamWriter
from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional


@dataclass
class Response:
    first_line: bytes
    headers: bytes
    body: bytes
    separator: Optional[bytes] = b'\r\n'

    def send(self, writer: StreamWriter):
        writer.write(self.first_line)
        writer.write(self.headers)
        writer.write(self.separator)
        writer.write(self.body)


def make_response(http_version, path, body: str, status: Optional[HTTPStatus] = HTTPStatus.OK) -> Response:
    body_len = len(body)
    first_line = f'{http_version} {status.value} {status.phrase}'.encode() + b'\r\n'
    headers = (
        b'Content-Type: application/json\r\n'
        b'Accept: application/json; encoding=utf8\r\n'
        b'Connection: close\r\n'
        b'Access-Control-Allow-Origin: *\r\n'
        b'Access-Control-Allow-Methods: *\r\n'
        b'Content-Length:' + f'{body_len}'.encode() + b'\r\n'
    )
    return Response(first_line=first_line, headers=headers, body=body.encode())
