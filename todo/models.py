from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TODO(models.Model):
    title = models.CharField("Title", max_length=200)
    details = models.TextField('Details')
    favorite = models.BooleanField("Bookmark", default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Date Published', default=timezone.now)

    class Meta:
        verbose_name = "TODO details"
        verbose_name_plural = "TODO details"
