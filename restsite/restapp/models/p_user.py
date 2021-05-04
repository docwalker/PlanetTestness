from django.db import models
from .p_group import P_Group

class P_User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    userid = models.CharField(max_length=550)
    groups = models.ManyToManyField(P_Group)

