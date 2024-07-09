from django.db import models

from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(default=0, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")

    def __str__(self):
        return f"Modelo:{self.modelo} - Ano:${self.ano} - Cor:{self.cor}"
