from django.db import models

# Categorias disponíveis no depósito
CATEGORIAS = [
    ("pneus", "Pneus"),
    ("pecas_viaturas", "Peças de Viaturas"),
    ("pecas_equipamentos", "Peças de Equipamentos"),
    ("filtros", "Filtros"),
    ("lubrificantes", "Lubrificantes"),
    ("fluidos", "Fluidos"),
    ("baterias", "Baterias"),
    ("laminas", "Lâminas"),
    ("fps", "FPS"),
]


class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)  # Ex: PN-1000R20
    categoria = models.CharField(max_length=30, choices=CATEGORIAS)
    quantidade = models.IntegerField(default=0)
    unidade = models.CharField(max_length=20, default="un")  # un, litros, etc.
    siscofis = models.CharField(
        max_length=50, blank=True, null=True, help_text="Número da ficha SISCOFIS"
    )
    localizacao = models.CharField(
        max_length=100, blank=True, null=True, help_text="Localização no depósito"
    )
    imagem = models.ImageField(
        upload_to="estoque/", blank=True, null=True, help_text="Foto do item"
    )

    def __str__(self):
        return f"{self.nome} ({self.codigo})"
