from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import RealEstate, Owner, Buyer, Image
from django import forms
from dataclasses import field


TYPE_CHOICES = [('ПРОДАЖА', 'Купить'), ('АРЕНДА', 'Снять')]
CATEG_CHOICES = [(key['category_id'], key['category__title']) for key in RealEstate.objects.values('category_id', 'category__title').distinct()]
AREA_CHOICES = [(key['area_id'], key['area__area_name']) for key in RealEstate.objects.values('area_id', 'area__area_name').distinct()]


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class FilterRealEstate(forms.Form):
    type_real_estate = forms.ChoiceField(label='Тип услуги', widget=forms.Select(attrs={'class': 'form-control', 'style': 'height: 50px; background-color: #dde2e3;'}), choices=TYPE_CHOICES)
    category = forms.ChoiceField(label='Тип недвижимости', widget=forms.Select(attrs={'class': 'form-control', 'style': 'height: 50px; background-color: #dde2e3;'}), choices=CATEG_CHOICES, required=False)
    number_of_rooms = forms.IntegerField(label='Кол-во комнат', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 50px; background-color: #dde2e3;', 'placeholder': 'Кол-во комнат'}), required=False)
    price = forms.CharField(label='Цена до', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 50px; background-color: #dde2e3;', 'placeholder': 'Цена до'}), required=False)
    area = forms.ChoiceField(label='Район', widget=forms.Select(attrs={'class': 'form-control', 'style': 'height: 50px; background-color: #dde2e3;'}), choices=AREA_CHOICES, required=False)
    total_area = forms.CharField(label='Площадь', widget=forms.TextInput(attrs={'class': 'form-control'}))


class FullFilterRealEstate(forms.Form):
    type_real_estate = forms.ChoiceField(label='Тип услуги', widget=forms.Select(attrs={'class': 'form-control'}), choices=TYPE_CHOICES)
    category = forms.ChoiceField(label='Тип недвижимости', widget=forms.Select(attrs={'class': 'form-control'}), choices=CATEG_CHOICES, required=False)
    number_of_rooms = forms.IntegerField(label='Кол-во комнат', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    price = forms.CharField(label='Цена до', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    area = forms.ChoiceField(label='Район', widget=forms.Select(attrs={'class': 'form-control'}), choices=AREA_CHOICES, required=False)
    total_area = forms.CharField(label='Площадь', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)


class UserStayOwner(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label='Пол',
        widget=forms.RadioSelect,
        choices=[(0, 'Ж'), (1, 'М')],
    )
    series = forms.CharField(label='Серия паспорта', widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(label='Номер паспорта', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.RegexField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}), regex=r'^\+?1?\d{9,15}$')

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'surname', 'gender', 'series', 'number', 'phone')


class UserRequest(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['first_name', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
        }


class AddRealEstateForm(forms.Form):
    type_real_estate = forms.ChoiceField(label='Тип услуги', widget=forms.Select(attrs={'class': 'form-control'}), choices=TYPE_CHOICES)
    category = forms.ChoiceField(label='Тип недвижимости', widget=forms.Select(attrs={'class': 'form-control'}), choices=CATEG_CHOICES)
    description = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'class': 'form-control'}))
    number_of_rooms = forms.IntegerField(label='Кол-во комнат', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(label='Цена', widget=forms.TextInput(attrs={'class': 'form-control'}))
    area = forms.ChoiceField(label='Район', widget=forms.Select(attrs={'class': 'form-control'}), choices=AREA_CHOICES)
    total_area = forms.CharField(label='Площадь', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))
    floor = forms.CharField(label='Этаж', widget=forms.TextInput(attrs={'class': 'form-control'}))
    max_floor = forms.CharField(label='Всего этажей', widget=forms.TextInput(attrs={'class': 'form-control'}))
