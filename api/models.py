import uuid

from django.db import models
from users.models import User

# Create your models here.


class Collection(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creator_network = models.TextField()


class NFT(models.Model):
    asset_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=200)
    picture = models.URLField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    supply = models.CharField(max_length=200)
    royalties = models.CharField(max_length=200)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    buyer = models.TextField(null=True, blank=True)