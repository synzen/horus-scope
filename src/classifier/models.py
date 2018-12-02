from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

def upload_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

class Item(models.Model):
    image = ResizedImageField(upload_to=upload_image)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True 
    )

class Prediction(models.Model):
    name = models.CharField(max_length=100)
    probability = models.FloatField()
    summary = models.TextField()
    item = models.ManyToManyField(Item)
