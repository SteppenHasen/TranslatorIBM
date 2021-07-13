from django import forms

class InputTextForm(forms.Form):
    to_translate_text = forms.CharField(widget=forms.Textarea) 