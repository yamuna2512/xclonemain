from django import forms
from .models import X

class XForm(forms.ModelForm):
  class Meta:
    model = X
    fields = '__all__'