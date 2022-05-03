from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from core_apps.articles.models import Article
from core_apps.articles.serializers import ArticleCreateSerializer

from .exceptions import AlreadyFavoritedException
from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def post(self, request, slug):
        data = request.data
        article = Article.objects.get(slug=slug)
        user = request.user

        favorite_exists = Favorite.objects.filter(user=user, article=article.pkid).exists()

        if favorite_exists:
            raise AlreadyFavoritedException
        else:
            data["article"] = article.pkid
            data["user"] = user.pkid
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            data = serializer.data
            data["message"] = "Article added to favorites."
            return Response(data, status=status.HTTP_201_CREATED)


class ListUserFavoriteArticlesAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        favorites = Favorite.objects.filter(user_id=request.user.pkid)

        # favorite_articles = [f.article for f in favorites]
        favorite_articles = []

        for favorite in favorites:
            article = Article.objects.get(pkid=favorite.article.pkid)
            serializer = ArticleCreateSerializer(
                article, context={"article": article.slug, "request": request}
            )
            article_data = serializer.data
            favorite_articles.append(article_data)
        data = {"favorite_articles": favorite_articles}
        return Response(data=data, status=status.HTTP_200_OK)
