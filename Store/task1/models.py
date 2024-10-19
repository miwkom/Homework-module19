from django.db import models


class Buyer(models.Model):
    username = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.username


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyer')

    def __str__(self):
        return self.title
