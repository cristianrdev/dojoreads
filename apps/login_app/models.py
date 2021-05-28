from django.core.exceptions import ValidationError
from django import forms
from django.db import models
import re
from django.contrib.auth.hashers import make_password, check_password
from datetime import date



MIN_FIELD_LENGHT = 2
def ValidarLongitudMinima(cadena):
    if len(cadena) < MIN_FIELD_LENGHT:
        raise forms.ValidationError(
            f'Error: {cadena} deberia tener mas de {MIN_FIELD_LENGHT} caracteres'
        )

def ValidarLongitudPassword(cadena):
    if len(cadena) < 8:
        raise forms.ValidationError(
            f'Error: la contraseña al menos debe contener 8 caracteres'
        )




def validarEmail(cadena):
    #valida que el email tenga el formato correcto
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not EMAIL_REGEX.match(cadena):          
        raise forms.ValidationError(
            f'Error de formato: {cadena} no es un e-mail valido'
        )
    #valida que el email no se repita
    
    for s in User.objects.all():
            # se usa .lower() para ovbiar las mayúsculas en la comparación de palabras
            if cadena.lower() == s.email.lower(): 
                raise forms.ValidationError(
                f'Error: el email {cadena} ya existe en nuestros registros!'
                )


def validarFecha(fecha):
    print(fecha)
    date_today = date.today() #fecha hoy 
    birth_date = str(fecha).split('-')
  
    birth_year = int(birth_date[0]) #año nacimieno
    birth_month = int(birth_date[1]) #mes de nacimiento
    birth_day = int(birth_date[2]) #día de nacimiento

    
    print(birth_date)
    birth_date_user = date(birth_year, birth_month, birth_day )
    days_has_passed = (date_today-birth_date_user).days
    # valida la edad mayor a 13 años
    if days_has_passed < (365.2425*13): #aqui se cambia la edad de acceso---------------------
            raise forms.ValidationError(
            f'Error: la fecha de nacimiento debe ser mayor de 13 años'
            )




# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitudMinima])
    last_name = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitudMinima] )
    birth_date = models.DateField(validators=[validarFecha])
    email = models.CharField(max_length=50, validators=[validarEmail])
    password = models.CharField(max_length=100, validators=[ValidarLongitudPassword])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # liked_books = a una lista de libros que le gustan a un usuario determinado
    # books_uploaded = una lista de libros cargados por un usuario determinado

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    @staticmethod
    def authenticate(email, password):
        user = User.objects.filter(email = email)
        print ('user', user)
        #buscar si hay un email en la base de datos
        if len(user) == 1:
            #si existe un email asociado
            #se existe un el usuario (se supone que debe ser uno solo por sus validaciones)
            user = user[0]
            bd_password = user.password
            if check_password(password, bd_password): #convierte los hash y los comparas
                return user
        print("usuario incorrecto")
        
        return None 

    





