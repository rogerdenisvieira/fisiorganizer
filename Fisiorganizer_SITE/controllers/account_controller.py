from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Fisiorganizer_SITE.controllers import main_controller, account_controller
from Fisiorganizer_SITE.models import UserExtra
from Fisiorganizer_SITE.forms import LoginForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # check if request user exists
        if User.objects.filter(username=username).exists():

            # store user who is trying to authenticate
            user_to_lock = User.objects.get(username=request.POST['username'])

            # return user's extra informations
            extra = UserExtra.objects.get(id_user=user_to_lock)

            # check if attemps to login are less than config file
            if extra.attempts < getattr(settings, "TENTATIVAS_LOGIN", None):

                # try to authenticate
                user = authenticate(username=username, password=password)

                # if user was authenticated
                if user is not None:
                    # if user is active
                    if user.is_active:
                        login(request, user)
                        messages.success(request, 'Seja bem-vindo ' + user.username, extra_tags='alert-success')
                        return redirect(main_controller.index)
                    else:
                        message = 'Usuário inativo.'
                else:
                    message = 'Falha na autenticação.'
                    extra.attempts += 1
                    extra.save()
            else:
                message = 'Seu usuário foi bloqueado. Entre em contato com o administrador.'
        else:
            message = 'Usuário inválido'

        # retrieve login page with messages
        messages.warning(request, message, extra_tags='alert-warning')
        return redirect(account_controller.login_user)
    else:
        form = LoginForm
        return render(request, 'login.html', {'LoginForm': form})

# logs out user
def logout_user(request):
    messages.success(request, 'Logout realizado com sucesso.', extra_tags='alert-success')
    logout(request)
    return redirect(main_controller.index)