from django.db import models

# Create your models here.

class Post(models.Model):
    judul = models.CharField(max_length=300)
    isi = models.TextField()

    def __str__(self):
        return f"{self.judul}"