from django.contrib.auth import get_user_model
from django.db import models

from core_apps.common.models import TimeStampedUUIDModel
from core_apps.articles.models import Article
from core_apps.profiles.models import Profile


class Comment(TimeStampedUUIDModel):
    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        return f"comment_{self.pk} to {self.article} by {self.author}"
