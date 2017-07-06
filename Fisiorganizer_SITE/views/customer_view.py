from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Fisiorganizer_SITE.forms import CustomerForm


@login_required
def create(request):
    customer_form = CustomerForm()

    if request.method == 'POST':
        # TODO implement persistence of customer
        print('it was a post')
    else:
        return render(request, 'customer/customer_create.html', {'customerForm': customer_form})


def edit(request):
    return HttpResponse("editar aluno")


def delete(request):
    return HttpResponse("excluir aluno")


def details(request):
    return HttpResponse("ver")


def list(request):
    return HttpResponse("listar")
