from django import forms
from .models import Chaivariety

class chaiform(forms.Form):
    your_chai_variety=forms.ModelChoiceField(queryset=Chaivariety.objects.all(),label='select chai variety')