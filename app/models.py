from django.db import models

# Create your models here.


class Url(models.Model):
    long_url = models.CharField(max_length=250)
    short_url = models.CharField(max_length=150)
    num = models.BigIntegerField(max_length=10)

    def __str__(self):
        return self.long_url + " " + self.short_url + " " + str(self.num)
