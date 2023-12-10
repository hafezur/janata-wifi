from django import forms 
from first_app.models import back_mart
class back_martForm(forms.ModelForm):
    class Meta:
        model=back_mart
        fields=['date','trade_code','high','low','open','close','volume']