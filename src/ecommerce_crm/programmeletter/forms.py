"""
Forms of programmeletter are ..
"""
from django import forms

from ecommerce_crm.programmeletter.models import TeamName
from ecommerce_crm.programmeletter.models import StaffInTeam

from ecommerce_crm.catalog.models import Category

from ecommerce_crm.suspense.models import Staff

from ajax_select import make_ajax_field


class StaffInTeamForm(forms.ModelForm):
    """
    Form for selecting staff for team.
    """
    # staff = forms.ModelChoiceField(queryset=Staff.objects.all())
    staff = make_ajax_field(StaffInTeam, 'staff', 'staff')

    def __init__(self, *args, **kwargs):
         super(StaffInTeamForm, self).__init__(*args, **kwargs)
         self.fields['staff'].widget.attrs={'class':'form-control'}


class TeamNameForm(forms.ModelForm):
    """
    Form for adding team for field work.
    """
    team_name = forms.CharField()
    def __init__(self, *args, **kwargs):
         super(TeamNameForm, self).__init__(*args, **kwargs)
         self.fields['team_name'].widget.attrs={'class':'form-control'}