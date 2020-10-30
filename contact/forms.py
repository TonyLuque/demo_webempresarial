from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class':'nombre_clase', 'placeholder': 'Arturo Rivera'} # Se usa para que Django añada las propiedades al crear el html
    ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'placeholder':'demo@demomail.com'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={'class':'nombre_clase', 'rows':3, 'placeholder': 'Escribe tu mensaje'} # Se usa para que Django añada las propiedades al crear el html
    ), min_length=10, max_length=1000)