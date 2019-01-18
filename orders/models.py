
from django.db import models


# Create your models here.

class Orders(models.Model):
    usertoken = models.CharField(max_length=40)
    orderno = models.CharField(unique=True, max_length=40)
    orderamount = models.DecimalField(max_digits=65535, decimal_places=65535)
    created_at = models.BigIntegerField(blank=True, null=True)
    is_filled = models.IntegerField(blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    source_id=models.IntegerField(blank=True,null=True)

    """def get_dict(self):
    	d={
    		"usertoken":self.usertoken,
    		"orderno":self.orderno,
    		"orderamounter":self.orderamounter,
    		"created_at":self.created_at,
    		"is_filled":sel.is_filled,
    		"service_type":self.service_type,
    		"source_id":self.source_id
    	}
    	return d"""

    class Meta:
    	managed=False
    	db_table='orders'