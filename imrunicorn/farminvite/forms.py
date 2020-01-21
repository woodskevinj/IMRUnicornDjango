from django import forms
from .models import InviteListing


class InviteListingForm(forms.ModelForm):

    class Meta:
        model = InviteListing
        fields = ('Invite_Date', 'Desired_Time_Slot',
                  'MDShooters_Name', 'Real_Name', 'Phone_Number', 'EMail')

