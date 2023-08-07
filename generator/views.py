from django.shortcuts import render
import random


# Create your views here.
def home(request):
    """
    Домашняя страница
    """
    return render(request, 'generator/home.html')


def about(request):
    """
    Сайт с описанием
    """
    return render(request, 'generator/about.html')


def password(request):
    """
    Генерируем пароль в зависимости от выбранных условий
    """
    # список символов по умолчанию
    characters = []

    # добавляем условие выбора букв
    if request.GET.get('letter'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))

    # добавляем условие если выбран верхний регистр
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # добавляем условие для спец символов
    if request.GET.get('special'):
        characters.extend(list('#!@$%^&*()-_+=;:,./?\|`~[]{}'))

    # добавляем условие для цифр
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # берет значение из select с именем length и задаёт длину пароля, по умолчанию 12.
    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        if len(characters) == 0:
            thepassword = 'Данные не выбраны'
        else:
            thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
