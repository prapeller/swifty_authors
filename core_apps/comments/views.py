from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from core_apps.articles.models import Article
from .models import Comment
from .serializers import CommentListSerializer, CommentSerializer


def _get_article_by_slug(slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        raise NotFound("That article does not exist in our catalog")
    return article


def _get_comment(id):
    try:
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        raise NotFound("Comment does not exist")
    return comment


class CommentListCreateAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get(self, request, **kwargs):
        article = _get_article_by_slug(slug=self.kwargs.get("article_slug"))
        comments = Comment.objects.filter(article_id=article.pkid)
        serializer = CommentListSerializer(comments, many=True,
                                           context={"request": request})
        data = {
            "num_comments": len(serializer.data),
            "comments": serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        article = _get_article_by_slug(slug=self.kwargs.get("article_slug"))
        data = request.data
        author = request.user
        data["author"] = author.pkid
        data["article"] = article.pkid
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CommentUpdateDeleteAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def put(self, request, comment_id):
        comment_to_update = _get_comment(comment_id)
        data = request.data
        serializer = self.serializer_class(comment_to_update,
                                           data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            "message": "Comment updated successfully",
            "comment": serializer.data,
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, comment_id):
        comment_to_delete = _get_comment(comment_id)
        comment_to_delete.delete()
        data = {"message": "Comment deleted successfully!"}
        return Response(data=data, status=status.HTTP_200_OK)
