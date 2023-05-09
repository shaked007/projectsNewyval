from django.db import models

# Create your models here.
class Check(models.Model):

    title = models.CharField(max_length=200, default='default')

    MY_LOCATIONS = (
         ('מצודת ציון', 'מצודת ציון'),
        ('מרגנית', 'מרגנית'),
        ('בניין מטכ"ל', 'בניין מטכ"ל'),
        )
        
    location = models.CharField(max_length=100, choices= MY_LOCATIONS,default=MY_LOCATIONS[0])
    MY_CHOICES = (
         ('VC', 'VC'),
        ('מצודה וחמ"לים', 'מצודה וחמ"לים'),
        ('VIP', 'VIP'),
        ('תשתיות', 'תשתיות'),
    )
    mahlaka = models.CharField(max_length=100, choices= MY_CHOICES, default=MY_CHOICES[0])
    isCritical = models.BooleanField(default = False)
    def __str__(self):
        return ("{} - {}".format(self.title, self.mahlaka))