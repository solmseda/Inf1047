from django.db import models

class MTCars(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.TextField(null=False)
    MPG = models.FloatField(null=False)
    CYL = models.IntegerField(null=False)
    DISP = models.FloatField(null=False)
    HP = models.IntegerField(null=False)
    DRAT = models.FloatField(null=False)
    WT = models.FloatField(null=False)
    QSEC = models.FloatField(null=False)
    VS = models.IntegerField(null=False)
    AM = models.IntegerField(null=False)
    GEAR = models.IntegerField(null=False)
    CARB = models.IntegerField(null=False)

class Meta:
    managed = True
    db_table = 'MTCars'
    ordering = ['ID']

def __self__(self):
    return self.NAME