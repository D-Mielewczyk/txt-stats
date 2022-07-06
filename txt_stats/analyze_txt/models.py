from django.db import models


# Create your models here.
class TextInput(models.Model):
    title = models.CharField(max_length=2000)
    text = models.TextField()
    case_sensitive = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title
