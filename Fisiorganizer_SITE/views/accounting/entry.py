from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Fisiorganizer_SITE.forms import AccountingEntryForm, ExerciseForm
from Fisiorganizer_SITE.models import AccountingEntry, AccountingEntryCategory, AccountingEntryType, Session
from Fisiorganizer_SITE.views.accounting import entry

@login_required
def create(request):


    if request.method == 'POST':
        accounting_entry_form = AccountingEntryForm(request.POST)
        if accounting_entry_form.is_valid():
            accounting_entry = accounting_entry_form.save(commit=False)
            accounting_entry.type = request.POST['id_type']
            accounting_entry.category = request.POST['id_category']
            accounting_entry.amount = request.POST['amount']
            accounting_entry.date = request.POST['date']
            accounting_entry.description = request.POST['description']
            accounting_entry.save()

            print('saving accounting entry into db')
            return redirect(entry.list)
        else:
            print(accounting_entry_form.errors)
    else:
        accounting_entry_form = AccountingEntryForm()
        return render(request, 'accounting/entry/create.html', {'accountingEntryForm': accounting_entry_form})

def edit(request):
    return HttpResponse("editar")


def delete(request):
    return HttpResponse("excluir")


def details(request):
    return HttpResponse("ver")


def list(request):
    return HttpResponse("listar")