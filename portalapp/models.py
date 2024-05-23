from django.db import models
from django.contrib.auth.models import User;
from django.utils import timezone

# Create your models here.

class CustomerDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unique_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50)
    gst = models.CharField(max_length=15, blank=True, null=True)
    allowed_meeting_participants = models.IntegerField(default=0)
    subscription_start_date = models.DateField()
    subscription_end_date = models.DateField()
    subscription_allowed_minutes = models.IntegerField(default=0)
    subscription_amount = models.DecimalField(max_digits=10, decimal_places=2)
    subscription_is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    
class CustomerMeetings(models.Model):
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    meeting_name = models.CharField(max_length=255)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField()
    max_members_joined = models.IntegerField()
    meeting_creator_name = models.CharField(max_length=255)
    participants = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    moderator_url = models.URLField()
    member_url = models.URLField()
    organization_id = models.CharField(max_length=100)
    configurations = models.TextField()
    current_members = models.IntegerField(default=0)
    end_date = models.DateField()
    meeting_status = models.CharField(max_length=50)

    def __str__(self):
        return self.meeting_name