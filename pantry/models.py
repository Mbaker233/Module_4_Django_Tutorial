from django.db import models


class FoodItem(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    expiration_date = models.DateField()

    def __str__(self):
        return self.item_name