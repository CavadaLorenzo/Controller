from django.db import models
from django.utils import timezone


# Create your models here.
class Transfer(models.Model):
    filename = models.CharField(max_length=500)
    from_server = models.CharField(max_length=25)
    to_server = models.CharField(max_length=25)
    transfer_date = models.DateTimeField(default=timezone.now)
    time = models.CharField(max_length=100)

    def __str__(self):
        return str("Transfer made from the request of: " + str(self.transfer_date))

class TransferRequest(models.Model):
    view_count = models.IntegerField()
    time_span = models.CharField(max_length=10)
    transfer_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str("Request made: " + str(self.transfer_date))
