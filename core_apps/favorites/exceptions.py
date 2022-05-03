from rest_framework.exceptions import APIException


class AlreadyFavoritedException(APIException):
    status_code = 400
    default_detail = "You've already made this article favor!"
