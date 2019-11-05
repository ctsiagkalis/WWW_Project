from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    BTC = models.CharField(max_length=200, unique=True, null=True)
    ETH = models.CharField(max_length=200, unique=True, null=True)
    LTC = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return f"User id: {self.id}, email: {self.email}, password: {self.password},\
            BTC: {self.BTC}, ETH: {self.ETH}, LTC: {self.LTC}"