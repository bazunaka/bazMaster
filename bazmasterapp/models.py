from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)