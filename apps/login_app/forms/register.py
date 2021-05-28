from django.forms import ModelForm
from django import forms
from ..models import User
from django.forms import widgets



class UserForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    password=forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control", "style":"width: 50%;"}), label='Contraseña')
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control", "style":"width: 50%;"}), label='Confirme su contraseña')
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
                'first_name': forms.TextInput(attrs = {"class":"form-control", "placeholder": "Ingrese su nombre", "style":"width: 50%;"}),
                'last_name': forms.TextInput(attrs = {"class":"form-control ","placeholder": "Ingrese su apellido", "style":"width: 50%;"}),
                'email': forms.TextInput(attrs = {"class":"form-control ", "style":"width: 70%;"}),                

                'birth_date' : forms.DateInput(
                    attrs={
                        'type': 'date',
                        'autocomplete' : 'off',
                        'input_format' : "%Y/%m/%d",
                        'class': 'form-control',
                        "style":"width: 50%;"
                    }
                ),
            }
    
        labels = {
                'first_name': "Nombre",
                'last_name': "Apellido",
                'birth_date': "Fecha de Nacimiento",
                'email': "Correo Electronico",
                'password': "Contraseña",
                'confirm_password': "Confirme su contraseña"

        }

    def clean(self):
            cleaned_data = super(UserForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError(
                    "Error: La contraseña de confirmación no coincide"
                )
        

