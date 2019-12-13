from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import Sum
from .models import Ganho
from despesa.models import Despesa

# Create your views here.
def total(request): 
    total_ganho = Ganho.objects.aggregate(Sum('valor'))['valor__sum']
    total_despesa = Despesa.objects.aggregate(Sum('valor'))['valor__sum']
    total = total_ganho - total_despesa
    context = {
        'total_despesa': "{:.2f}".format(total_despesa),
        'total_ganho': "{:.2f}".format(total_ganho),
        'total': "{:.2f}".format(total)
    }

    return render(request, 'ganho/total.html', context=context)
