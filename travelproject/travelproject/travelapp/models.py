from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='photos')
    dist = models.TextField()

    def __str__(self):
        return self.name