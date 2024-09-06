from django.db import models

class Item(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)

    class Meta:
         db_table = 'employees'