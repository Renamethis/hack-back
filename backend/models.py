from django.db import models

class Temp(models.Model):
    class Meta:
        db_table = 'temp'
        verbose_name = 'Temp'
        verbose_name_plural = 'Temp'

    id = models.CharField(max_length=512, primary_key=True)