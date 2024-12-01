from django import forms

class NewPageForm(forms.Form):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a title for the page'
        })
    )
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Enter the content for the page'
        })
    )