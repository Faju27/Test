from django import forms

from new_app.models import Blogger


class BloggerForm(forms.ModelForm):

    class Meta:
        model = Blogger
        fields = ("name",  "phone")
        labels = {
            'name': 'Enter Name',
            'phone': 'Enter Phone No',
        }