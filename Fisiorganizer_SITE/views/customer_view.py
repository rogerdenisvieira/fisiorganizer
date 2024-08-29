from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Fisiorganizer_SITE.forms import CustomerForm
from Fisiorganizer_SITE.models import Customer
from Fisiorganizer_SITE.views import customer_view


@login_required
def create(request):
    customer_form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.name = request.POST['name']
            customer.address = request.POST['address']
            customer.city = request.POST['city']
            customer.cellphone = request.POST['cellphone']
            customer.age = request.POST['age']
            customer.details = request.POST['details']
            customer.save()

            print('object saved')
            return redirect(customer_view.list)
        else:
            print(form.errors)
    else:
        return render(request, 'customer/customer_create.html', {'customerForm': customer_form})

@login_required
def edit(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)

        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.name = request.POST['name']
            customer.address = request.POST['address']
            customer.city = request.POST['city']
            customer.cellphone = request.POST['cellphone']
            customer.age = request.POST['age']
            customer.details = request.POST['details']
            customer.save()

            return redirect(customer_view.list)
    else:
        customer_form = CustomerForm(instance=customer)
        return render(request, 'customer/customer_edit.html', {'customer_form': customer_form, 'customer':customer })

@login_required
def delete(request):
    customerId = request.POST['id']
    Customer.objects.filter(id=customerId).delete()
    return HttpResponse("excluir aluno")

@login_required
def details(request, id):
    customer = get_object_or_404(Customer, id=id)

    dto = {
        'Nome': customer.name,
        'Endereço': customer.address,
        'Celular': customer.cellphone,
        'Idade': customer.age,
        'Detalhes': customer.details
    }

    return render(request, 'customer/customer_details.html', {'dto': dto.items()})

@login_required
def list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})
