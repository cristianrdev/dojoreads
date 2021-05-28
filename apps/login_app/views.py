
from django.shortcuts import render, redirect
from .models import User
#importar los forms 
from .forms.register import UserForm
from .forms.login import LoginForm

# Create your views here.
def index(request):
    # si se carga el index por medio de un get
    if request.method == 'GET':
        # si no existe la sesión se muestra los forms y se hace render de log_register_page.html
        if 'id' not in  request.session :
            #presentar RegisterForm
            form = UserForm()
            #presentar LoginForm
            loginForm = LoginForm()
            return render(request, 'log_register_page.html', {"form" : form, 'loginForm': loginForm})
        # si existe la sesión se redirecciona a la app_favourite_books
        else:
            return redirect('/books') #cambiar acá segun la app----------------------------------


def register(request):
    print("es post"*50)
    form = UserForm(request.POST)
    loginForm = LoginForm()
    if form.is_valid():
        print('es valido'*20)
        user = form.save()
        request.session['id'] = user.id
        print(request.session['id'])
        return redirect('/books') #cambiar acá segun la app----------------------------------
    else:
        return render(request, 'log_register_page.html', {"form" : form, 'loginForm': loginForm})


def login(request):
    form = UserForm()
    loginForm = LoginForm(request.POST)
    # si el form es valido
    if loginForm.is_valid():
        #guarda en user la clase 
        user = loginForm.login(request.POST)

        if user:
            request.session['id'] = user.id
            return redirect("/books") #cambiar acá segun la app------------------------------------
    
    message_error = "Usuario y/o contraseña incorrectos"
  
    return render(request, 'log_register_page.html', {"form" : form, 'loginForm': loginForm , "message_login_failed" : message_error } ) 

def logout(request):
    request.session.delete()
    return redirect('/')