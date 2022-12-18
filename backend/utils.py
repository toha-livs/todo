from asyncio import StreamWriter
from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional


@dataclass
class Response:
    first_line: bytes
    headers: bytes
    body: bytes

    def send(self, writer: StreamWriter):
        writer.write(self.first_line)
        writer.write(self.headers)
        writer.write(b'\n')
        writer.write(self.body)


def make_response(path, body: str, status: Optional[HTTPStatus] = HTTPStatus.OK) -> Response:
    body_len = len(body)
    first_line = f'HTTP/1.1 {path} {status.value} {status.phrase}'.encode()
    headers = (
        b'Content-Type: application/json\n'
        b'Accept: application/json; encoding=utf8\n'
        b'Connection: close\n'
        b'Access-Control-Allow-Origin: *\n'
        b'Access-Control-Allow-Methods: *\n'
        b'Content-Length:' + f'{body_len}'.encode() + b'\n'
    )
    return Response(first_line=first_line, headers=headers, body=body.encode())
