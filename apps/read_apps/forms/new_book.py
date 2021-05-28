from os import name
from django import forms
from django.forms import ModelForm, Textarea
from django import forms
from django.db import models
from django.forms import widgets
from apps.read_apps.models import Book, Author, Review



class AuthorForm(forms.Form):
    # all_authors = Author.objects.all()
    # aa = [(None,'--Autor existente--')]
    # for a in all_authors:
    #     aa.append((a.name, a.name))

    # author = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.Select,
    #     choices=aa,
    #     label= "Autor ya existente"
    #      )

    # name = forms.CharField(required=False,label="... o puede añadir un  nuevo autor")   

    name =forms.CharField(widget=forms.TextInput(attrs = {"class":"form-control", "style":"width: 50%;"}), label="... o puede añadir un  nuevo autor", required=False)

class BookForm(ModelForm):
    class Meta:
        
        model = Book
        fields = {'title'}
        widgets ={
            'title' : forms.TextInput(attrs = {"class":"form-control", "style":"width: 50%;"}),
        }

class ReviewForm(ModelForm):
    class Meta:
        OPCIONES_TIPO= [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
        model = Review
        fields = '__all__'
        widgets ={
            'rating' : forms.Select(choices=OPCIONES_TIPO,attrs={"style":"width: 10%;"}),
            'review': Textarea(attrs = {'class':'form-control ', 'rows':"2", 'style':'resize: none; width: 40%;'}),
        }


