from django.db import models
from inventory.models import ItemEstoque

STATUS_CHOICES = [
    ("disponivel", "Disponível"),
    ("manutencao", "Em manutenção"),
    ("inoperante", "Inoperante"),
]


class Viatura(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="disponivel"
    )
    odometro = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"


class Equipamento(models.Model):
    numero_serie = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=100)  # ex: Retroescavadeira, Pá carregadeira
    horas_trabalhadas = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="disponivel"
    )

    def __str__(self):
        return f"{self.tipo} - {self.numero_serie}"


class Manutencao(models.Model):
    viatura = models.ForeignKey(
        Viatura, on_delete=models.CASCADE, null=True, blank=True, related_name="manutencoes"
    )
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.CASCADE, null=True, blank=True, related_name="manutencoes"
    )
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField()
    motivo = models.TextField()
    usuario = models.CharField(max_length=100)  # quem registrou a manutenção

    def __str__(self):
        alvo = self.viatura.placa if self.viatura else self.equipamento.numero_serie
        return f"Manutenção {alvo} - {self.data}"


class AplicacaoItem(models.Model):
    manutencao = models.ForeignKey(
        Manutencao, on_delete=models.CASCADE, related_name="itens", null=True, blank=True
    )
    servico = models.ForeignKey(
        "ServicoRealizado", on_delete=models.CASCADE, related_name="itens", null=True, blank=True
    )
    item = models.ForeignKey(ItemEstoque, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    liberado_por = models.CharField(max_length=100)

    def __str__(self):
        contexto = "Manutenção" if self.manutencao else "Serviço"
        return f"{self.quantidade}x {self.item.nome} -> {contexto}"


class ServicoRealizado(models.Model):
    viatura = models.ForeignKey(
        Viatura, on_delete=models.CASCADE, null=True, blank=True, related_name="servicos"
    )
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.CASCADE, null=True, blank=True, related_name="servicos"
    )
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField()
    observacoes = models.TextField(blank=True, null=True)
    usuario = models.CharField(max_length=100)  # quem registrou o serviço

    def __str__(self):
        alvo = self.viatura.placa if self.viatura else self.equipamento.numero_serie
        return f"Serviço {alvo} - {self.data}"
