from django.db import models


class DerivativeResult(models.Model):
    const = models.CharField()
    func = models.CharField(max_length=255)
    sequence = models.IntegerField(default=1)
    result = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DerivativeResult({self.const}, {self.func}, {self.sequence})"
