from django import forms
from django.forms import widgets
from ..models import User

#construimos un form usando las librerías de django ( que no depende de un objeto proveniente de models)
class LoginForm(forms.Form): # LoginForm hereda de (forms.Form) porque es un formulario que no viene de un models!!!
    email = forms.EmailField(widget= forms.TextInput(attrs = {"class":"form-control ", "style":"width: 50%;"}), max_length=50, required=True)
    password = forms.CharField( widget= forms.PasswordInput(attrs = {"class":"form-control ", "style":"width: 50%;"}), required=True)



    def login(self, request):
        # comprueba sus validaciones (las que definí arriba)
        email = self.cleaned_data.get('email') 
        password = self.cleaned_data.get('password')

        user = User.authenticate(email, password)  
        return user 