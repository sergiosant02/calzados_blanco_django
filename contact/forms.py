from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=50, required=True)
    email = forms.EmailField(label="Email", max_length=50, required=True)
    content = forms.CharField(label="Contenido", max_length=50, required=True, widget=forms.Textarea)