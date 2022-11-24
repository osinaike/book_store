from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, label="My title")
    isbn = forms.CharField(max_length=255)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
