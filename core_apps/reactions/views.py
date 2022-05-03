from rest_framework import permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from core_apps.articles.models import Article

from .models import Reaction
from .serializers import ReactionSerializer


def _find_article_by_slug(slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        raise NotFound(f"Article with the slug {slug} does not exist.")
    return article


class CreateDeleteReacteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReactionSerializer

    def set_reaction(self, article, user, reaction):
        try:
            existing_reaction = Reaction.objects.get(article=article,
                                                     user=user)
            existing_reaction.delete()
        except Reaction.DoesNotExist:
            pass

        data = {"article": article.pkid, "user": user.pkid,
                "reaction": reaction}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {"message": "Reaction successfully set"}
        status_code = status.HTTP_201_CREATED
        return response, status_code

    def post(self, request, *args, **kwargs):
        slug = self.kwargs.get("slug")
        article = _find_article_by_slug(slug)
        user = request.user
        reaction = request.data.get("reaction")

        try:
            existing_reaction = Reaction.objects.get(article=article,
                                                     user=user, reaction=reaction)
            existing_reaction.delete()
            response = {
                "message": f"Your {'LIKE' if reaction in [1, '1'] else 'DISLIKE'} was deleted."
            }
            status_code = status.HTTP_200_OK
        except Reaction.DoesNotExist:
            response, status_code = self.set_reaction(article, user, reaction)

        return Response(response, status_code)
