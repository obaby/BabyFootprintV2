# utils/custom_exception.py
from rest_framework import status
from rest_framework.views import exception_handler

from reminder.utils.json_response import ErrorResponse


class CustomException(Exception):
    _default_code = 400

    def __init__(
        self,
        message: str = "",
        status_code=status.HTTP_400_BAD_REQUEST,
        data=None,
        code: int = _default_code,
    ):

        self.code = code
        self.status = status_code
        self.message = message
        if data is None:
            self.data = {"detail": message}
        else:
            self.data = data

    def __str__(self):
        return self.message

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    # 这里对自定义的 CustomException 直接返回，保证系统其他异常不受影响
    if isinstance(exc, CustomException):
        return ErrorResponse(data=exc.data, status=exc.status)
    response = exception_handler(exc, context)
    return response