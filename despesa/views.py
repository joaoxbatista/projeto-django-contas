from django.shortcuts import render
from .serializer import DespesaSerializer
from rest_framework import generics
from .models import Despesa

class DespesaList(generics.ListCreateAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

class DespesaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer