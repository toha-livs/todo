from dataclasses import dataclass
from typing import Optional
from http import HTTPStatus


@dataclass
class BaseRequestError(BaseException):
    message: Optional[str] = 'Server error'
    code: Optional[int] = HTTPStatus.INTERNAL_SERVER_ERROR


class BadRequestError(BaseRequestError):
    message = 'Bad request'
    code = HTTPStatus.BAD_REQUEST


class NotFoundRequestError(BaseRequestError):
    message = 'Not found'
    code = HTTPStatus.NOT_FOUND
