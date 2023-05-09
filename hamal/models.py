from django.db import models
from check.models import Check

# Create your models here.
class Hamal(models.Model):
    Title = models.CharField(max_length=200)
    checkId = models.ForeignKey(Check, on_delete=models.CASCADE)
    def __str__(self):
        return ("{} - {} - {}".format(self.Title, self.checkId.title, self.checkId.mahlaka))