from django.urls import path
from .views import DespesaList, DespesaDetail

urlpatterns = [
    path('', DespesaList.as_view()),
    path('<int:pk>', DespesaDetail.as_view()),
]
