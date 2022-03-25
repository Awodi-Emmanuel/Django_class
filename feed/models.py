from django.db import models
from django.forms import CharField

# Create your models here.
class Post(models.Model):
  text = models.CharField(max_length=178, blank=False, null=False)

  def __str__(self):
    return self.text 