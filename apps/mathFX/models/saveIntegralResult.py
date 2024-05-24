from django.db import models


class IntegralResult(models.Model):
    constant = models.CharField()
    function = models.CharField(max_length=255)
    n1 = models.FloatField(null=True, blank=True)
    n2 = models.FloatField(null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    error = models.CharField(max_length=255, null=True, blank=True)
    is_definite = models.BooleanField(default=False)


