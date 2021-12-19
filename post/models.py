from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import datetime

from django.db.models.fields import NullBooleanField
from django.forms.widgets import NullBooleanSelect

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = datetime.datetime.now()
        self.save()

    def unpublish(self):
        self.published_date = None
        self.save()

    def __str__(self):
        return self.title