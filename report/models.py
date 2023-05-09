from django.db import models
from hamal.models import Hamal
from check.models import Check
# Create your models here.
class Report(models.Model):
    submitDate = models.CharField(max_length=200, blank = True)
    submitter = models.CharField(max_length=100)
    tkulim = models.JSONField(blank=True)
    checkId = models.ForeignKey(Check, on_delete=models.CASCADE)
    mahlaka = models.CharField(max_length=100)
    comment = models.CharField(max_length=300, blank = True)

    
    def __str__(self):
        return ("{} - {} - {}".format(self.checkId.title, self.mahlaka, self.submitDate))
