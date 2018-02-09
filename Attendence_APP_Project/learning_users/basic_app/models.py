from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.
CHOICES=[('morning','Morning'),('evening','Evening')]
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)
    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #For user session form
    session = models.CharField(max_length=25,choices=CHOICES, default="No Attendence")
    t_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
