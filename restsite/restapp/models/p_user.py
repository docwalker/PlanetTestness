from django.db import models
from .p_group import P_Group

class P_User(models.Model):
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    userid = models.CharField(max_length=550, primary_key=True)
    groups = models.ManyToManyField(P_Group, related_name="group", blank=True, null=True)

