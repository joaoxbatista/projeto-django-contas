from django.db import models
from django.contrib.auth.models import User

class Ganho(models.Model):

    class Meta:
        verbose_name_plural = 'ganhos'

    # Atributos
    data = models.DateField(auto_now=True, verbose_name='data_criacao')
    valor = models.DecimalField(max_digits=8,decimal_places=2)
    descricao = models.TextField()
    usuario = models.ForeignKey(User, related_name='ganhos', on_delete=models.CASCADE)

    def __str__(self):

        return str(self.data) + ' - ' + self.descricao

