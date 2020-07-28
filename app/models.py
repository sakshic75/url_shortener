from django.db import models

# Create your models here.


class Url(models.Model):
    long_url = models.CharField(max_length=250)

    num = models.BigIntegerField()
    unique_key = models.CharField(max_length=150)

    def __str__(self):
        return self.long_url + " " + self.unique_key + str(self.num)
