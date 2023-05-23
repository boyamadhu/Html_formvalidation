from django import forms

class topic_form(forms.Form):
    topic_name=forms.CharField(max_length=100)
    