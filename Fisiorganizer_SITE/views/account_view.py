from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Fisiorganizer_SITE.views import account_view, main_view
from Fisiorganizer_SITE.models import UserExtra
from Fisiorganizer_SITE.forms import LoginForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()
        if not user:
            messages.warning(request, 'Usuário inválido', extra_tags='alert-warning')
            return redirect(account_view.login_user)

        user_to_lock = User.objects.get(username=username)
        extra = UserExtra.objects.get(user_id=user_to_lock)

        if extra.attempts >= getattr(settings, "TENTATIVAS_LOGIN", None):
            messages.warning(request, 'Seu usuário foi bloqueado. Entre em contato com o administrador.', extra_tags='alert-warning')
            return redirect(account_view.login_user)

        user = authenticate(username=username, password=password)
        if user is None:
            extra.attempts += 1
            extra.save()
            messages.warning(request, 'Falha na autenticação.', extra_tags='alert-warning')
            return redirect(account_view.login_user)

        if not user.is_active:
            messages.warning(request, 'Usuário inativo.', extra_tags='alert-warning')
            return redirect(account_view.login_user)

        login(request, user)
        messages.success(request, f'Seja bem-vindo {user.username}', extra_tags='alert-success')
        return redirect(main_view.index)

    form = LoginForm()
    return render(request, 'login.html', {'LoginForm': form})

# logs out user
def logout_user(request):
    messages.success(request, 'Logout realizado com sucesso.', extra_tags='alert-success')
    logout(request)
    return redirect(main_view.index)