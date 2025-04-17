from django.db import models

# Create your models here.
class App (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    tecnology = models.CharField(max_length=200)
    craeted_at = models.DateTimeField(auto_now_add=True)