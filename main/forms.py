from django import forms

class CreateNewPost(forms.Form):
  title = forms.CharField(label='Title', max_length=50)
  description = forms.CharField(label='Description',max_length=1000, required=False)
  art = forms.ImageField()
