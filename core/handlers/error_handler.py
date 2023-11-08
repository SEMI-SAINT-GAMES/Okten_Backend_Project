from rest_framework.response import Response
from rest_framework.views import exception_handler

from core.enums.error_enum import ErrorEnum
from core.exeptions.jwt_exeption import JwtException


def error_handler(ext:Exception, context:dict)->Response:
    handlers = {
        'JwtException':_jwt_validation_error
    }
    responce = exception_handler(ext, context)
    ext_class = ext.__class__.__name__

    if ext_class in handlers:
        return handlers[ext_class](ext, context)
    return responce

def _jwt_validation_error(ext:JwtException, context:dict)->Response:
    return Response(*ErrorEnum.JWT.value)