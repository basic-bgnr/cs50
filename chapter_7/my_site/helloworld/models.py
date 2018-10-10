from django.db import models

# Create your models here.
class TimeDatabase(models.Model):
    city = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    
    def __str__(self):
        return "city: {}, date: {}, time: {}".format(self.city,
                                                     self.date,
                                                     self.time)


class TimeMaker(models.Model):
    name = models.CharField(max_length=64)
    
