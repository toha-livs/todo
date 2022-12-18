from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseRequestError(BaseException):
    message: Optional[str] = 'Server error'
    code: Optional[int] = 500


class BadRequestError(BaseRequestError):
    message = 'Bad request'
    code = 400


class NotFoundRequestError(BaseRequestError):
    message = 'Not found'
    code = 404
