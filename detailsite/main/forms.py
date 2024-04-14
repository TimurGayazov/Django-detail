from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, EmailInput, PasswordInput, FileInput, FloatField, CharField, ModelChoiceField
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class DetailForm(ModelForm):
    detail_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите название'}))
    detail_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'input-group form-control-file', 'type': 'file'}))
    detail_size = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите размер(ы)'}))
    detail_color = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите цвет(а)'}))
    detail_material = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите материал(ы)'}))
    detail_description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", 'placeholder': 'Введите описание', 'id': 'textareaform'}))

    class Meta:
        model = Detail
        fields = ['detail_name', 'detail_image', 'detail_size', 'detail_color', 'detail_material', 'detail_description']
        enctype = "multipart/form-data"