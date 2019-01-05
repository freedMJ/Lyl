from django.db import models


# Create your models here.

class Orders(models.Model):
    usertoken = models.CharField(max_length=40)
    orderno = models.CharField(unique=True, max_length=40)
    orderamount = models.DecimalField(max_digits=65535, decimal_places=65535)
    created_at = models.BigIntegerField(blank=True, null=True)
    is_filled = models.IntegerField(blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed =False
        db_table = 'orders'
