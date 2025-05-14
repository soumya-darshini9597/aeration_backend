from django.db import models


class Areation(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    state = models.CharField(max_length=450)

 