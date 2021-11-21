from django import forms

class myForm(forms.Form):
   username = forms.CharField(max_length=40,required=True)
   password = forms.CharField(max_length=30,widget=forms.PasswordInput)