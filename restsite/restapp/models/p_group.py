from django.db import models

class P_Group(models.Model):

    name = models.CharField(max_length=256, primary_key=True)
