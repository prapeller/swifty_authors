from rest_framework.exceptions import APIException


class NotYourArticle(APIException):
    status_code = 403
    default_detail = "You can't edit an article that doesn't belong to you!"
