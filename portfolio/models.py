from django.db import models

class Project(models.Model):
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to= 'prtfolio/image/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.titel
