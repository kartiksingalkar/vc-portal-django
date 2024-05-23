from django.contrib import admin

# Register your models here.

from .models import CustomerDetails, CustomerMeetings

admin.site.register(CustomerDetails)
admin.site.register(CustomerMeetings)