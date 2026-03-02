from django.db import models

class members(models.Model):
    member_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    join_date = models.DateField()


    def __str__(self):
        return self.name
