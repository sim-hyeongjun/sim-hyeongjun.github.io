from django import forms

class NewsSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')