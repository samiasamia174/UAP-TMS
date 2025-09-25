from django.db import models

# Create your models here.
from django.db import models


class Payment(models.Model):
    registration = models.OneToOneField('transport.Registration', on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, default="pending")
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.registration} - {self.status}"
