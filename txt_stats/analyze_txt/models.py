from django.db import models


# Create your models here.

class TextInput(models.Model):
    text = models.CharField(max_length=int(1e9))
    case_sensitive = models.BooleanField()
