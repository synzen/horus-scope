from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.

def upload_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

class ItemQuerySet(models.QuerySet):
    pass

class ItemManager(models.Manager):
    def get_queryset(self):
        return ItemQuerySet(self.model, using=self._db)

class Item(models.Model):
    image = ResizedImageField(upload_to=upload_image)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True 
    )

    objects = ItemManager()

class Prediction(models.Model):
    name = models.CharField(max_length=100)
    probability = models.FloatField()
    summary = models.TextField()
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
        null=True 
    )
