from django import forms
from datetime import date
from testapp.models import CHOICES
from testapp.models import UserSession


class UserSessionForm(forms.ModelForm):
    class Meta:
        model = UserSession
        fields = ('session','t_date')

    # session = forms.ChoiceField(choices=CHOICES)

    # CHOICES=[('morning','Morning'),('evening','Evening')]
    # session = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


    # date = forms.DateField(initial=date.today(), disabled=True)
