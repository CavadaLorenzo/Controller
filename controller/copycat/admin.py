from django.contrib import admin
from .models import Transfer, TransferRequest

"""
Added to admin page the Transfer model and the Transfer request module.
"""
admin.site.register(Transfer)
admin.site.register(TransferRequest)
