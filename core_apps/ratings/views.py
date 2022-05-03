from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from core_apps.articles.models import Article
from .exceptions import (AlreadyMadeArticleRatingException,
                         CantRateYourOwnArticleException, CantFindArticleException)
from .models import Rating


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_article_rating_view(request, article_id):
    current_user = request.user
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise CantFindArticleException

    if article.author == current_user:
        raise CantRateYourOwnArticleException

    if article.article_ratings.filter(rated_by__pkid=current_user.pkid).exists():
        raise AlreadyMadeArticleRatingException

    elif request.data.get("value") == 0:
        return Response(
            {"detail": "You can't give a zero rating"},
            status=status.HTTP_400_BAD_REQUEST),

    else:
        Rating.objects.create(
            article=article,
            rated_by=current_user,
            value=request.data.get("value"),
            review=request.data.get("review"),
        )

        return Response(
            {"success": "Rating has been added"},
            status=status.HTTP_201_CREATED,
        )
