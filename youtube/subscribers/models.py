from django.db import models

# Create your models here.


class Friend(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
