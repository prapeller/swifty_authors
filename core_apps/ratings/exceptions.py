from rest_framework.exceptions import APIException


class CantFindArticleException(APIException):
    status_code = 403
    default_detail = "Cant find article with this id!"

class CantRateYourOwnArticleException(APIException):
    status_code = 403
    default_detail = "You can't rate an article that belongs to you!"


class AlreadyMadeArticleRatingException(APIException):
    status_code = 400
    default_detail = "You've already rated this article!"
