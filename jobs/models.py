from django.db import models

# Create your models here.
# images


class Job(models.Model):
    # Images -accpept jpg
    # you need to install: pip3 install pillow
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.CharField(max_length=300)
