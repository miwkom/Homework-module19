from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Game, Buyer


def platform(request):
    title = 'Главное меню'
    context = {
        'title': title
    }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Витрина'
    games = Game.objects.all()
    context = {
        'title': title,
        'games': games
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'cart.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    context = {
        'info': '',
        'error': '',
        'form': UserRegistrationForm(),
    }
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                context['error'] = 'Пароли не совпадают!'
            elif len(password) < 8:
                context['error'] = 'Пароль должен быть не менее 8 символов!'
            elif Buyer.objects.filter(username=username).exists():
                context['error'] = 'Логин занят!'
            elif int(age) < 18:
                context['error'] = 'Вы не достигли 18 лет!'
            else:
                Buyer.objects.create(username=username, balance=0, age=age)
                context['info'] = f'Регистрация завершена,{username}!'

    else:
        form = UserRegistrationForm()
    return render(request, 'registration_page.html', context)

