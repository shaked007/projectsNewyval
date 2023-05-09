from django.db import models
from hamal.models import Hamal
# from django.contrib.postgres.fields import JSONField
# Create your models here.
class Tool(models.Model):
    comments = models.CharField(null=True,blank=True,max_length=200)
    CAUSES = (
        ('VC','VC'),
          ('SOC','SOC'),
            ('PC','PC'),
            ('תקנ"ם','תקנ"ם'),
            ('VIP','VIP'),
            ('מצודה וחמ"לים','מצודה וחמ"לים'),
            ('סיסטם','סיסטם'),
            ('מחכים לציוד','מחכים לציוד'),
            ('אחר','אחר'),
                

       
        )
    delayCause = models.CharField(null=True,blank=True, max_length=100, choices= CAUSES)
    Title = models.CharField(null=True,blank=True, max_length=200)
    type = models.CharField(max_length=100)
    hamalId = models.ForeignKey(Hamal, on_delete=models.CASCADE)
    ip = models.CharField(max_length=100,null=True,blank=True)

    boolChecks = models.JSONField(null=True,blank=True)
    info = models.JSONField(null=True,blank=True)

    # IsCritical = models.BooleanField(default = False)
    def __str__(self):
        return ("{} - {}".format(self.Title, self.hamalId))