from django.db import models

class Bank(models.Model):
    name_bank = models.CharField(max_length=100, verbose_name="Название банка", unique=True)