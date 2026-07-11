from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Board, Lista, Tarjeta


class RegisterForm(UserCreationForm):

    class Meta:

        model = User

        fields = [
            'username',
            'password1',
            'password2'
        ]


class BoardForm(forms.ModelForm):

    class Meta:

        model = Board

        fields = ['nombre']

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            })

        }


class ListaForm(forms.ModelForm):

    class Meta:

        model = Lista

        fields = ['nombre']

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            })

        }


class TarjetaForm(forms.ModelForm):

    class Meta:

        model = Tarjeta

        fields = [
            'titulo',
            'descripcion',
            'fecha_limite',
            'prioridad',
            'color',
            'etiqueta',
            'completada'
        ]

        widgets = {

            'titulo': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control'
            }),

            'fecha_limite': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'prioridad': forms.Select(attrs={
                'class': 'form-select'
            }),

            'color': forms.Select(attrs={
                'class': 'form-select'
            }),

            'etiqueta': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'completada': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),

        }