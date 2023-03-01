from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=200)
    year=models.IntegerField()
    desc=models.TextField()
    img=models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.name

