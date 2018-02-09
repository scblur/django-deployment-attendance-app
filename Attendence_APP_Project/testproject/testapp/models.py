from django.db import models
from django import forms
from datetime import datetime,date

# Create your models here.
CHOICES=[('morning','Morning'),('evening','Evening')]

class UserSession(models.Model):
    session = models.CharField(max_length=25,choices=CHOICES)
    # session = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    t_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.session + " " + str(self.t_date)
