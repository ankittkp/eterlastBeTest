from django.db import models

# Create your models here.


class User(models.Model):
    user = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

    def __repr__(self):
        return str(self.user)