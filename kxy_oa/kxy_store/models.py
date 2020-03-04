from django.db import models
class Store(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.text

class Product(models.Model):
    """this is our product"""
    text = models.CharField(max_length=200,db_column="product_name")
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.FloatField()
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    price = models.FloatField()
    unit =models.CharField(max_length=200)

    def __str__(self):
        return self.text
