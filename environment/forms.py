from django import forms
from datetime import date, timedelta


class SearchDataForm(forms.Form):
    start_date = forms.DateField(
        label='start date',
        required=True,
        initial=date.today() - timedelta(days=1)
    )
    end_date = forms.DateField(
        label='end date',
        required=True,
        initial=date.today()
    )
