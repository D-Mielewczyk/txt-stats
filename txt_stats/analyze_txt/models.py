from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TextInput(models.Model):
    title = models.CharField(max_length=2000)
    text = models.TextField()
    case_sensitive = models.BooleanField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
