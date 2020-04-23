from django.db import models
from django.utils import timezone

class Transfer(models.Model):
    """This model represent an executed Transfer. 

    :param filename: the name of the file copied (maximum lenght of 500 char) 
    :type filename: string
    :param from_server: the server from where the file have been copied
    :type filename: string
    :param to_server: the server where the file have been copied
    :type filename: string
    :param transfer_date: the date in timezone format when the transfer have been executed
    :type filename: timezone
    :param time: the time needed for the copy
    :type filename: timezone

    """
    filename = models.CharField(max_length=500)
    from_server = models.CharField(max_length=25)
    to_server = models.CharField(max_length=25)
    transfer_date = models.DateTimeField(default=timezone.now)
    time = models.CharField(max_length=100)

    def __str__(self):
        return str("Transfer made from the request of: " + str(self.transfer_date))

class TransferRequest(models.Model):
    """This model represent a request for a Transfer. 

    :param view_count: Number of time that a file need to be requested to justify the copy 
    :type filename: int
    :param time_span: the time interval in which the N requests have to be made
    :type filename: string
    :param transfer_date: the date in timezone format when the transfer request have been made
    :type filename: timezone
    """

    view_count = models.IntegerField()
    time_span = models.CharField(max_length=10)
    transfer_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str("Request made: " + str(self.transfer_date))
