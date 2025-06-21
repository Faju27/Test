from django import forms

from new_app.models import Blogger


class BloggerForm(forms.ModelForm):
    name = forms.CharField(label='Enter Name')
    phone_number = forms.CharField(label='Enter Phone No')

    class Meta:
        model = Blogger
        fields = ("name",  "phone_number")