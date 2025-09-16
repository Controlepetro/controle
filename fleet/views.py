from rest_framework import viewsets
from .models import Viatura, Equipamento, Manutencao, ServicoRealizado
from .serializers import (
    ViaturaSerializer,
    EquipamentoSerializer,
    ManutencaoSerializer,
    ServicoRealizadoSerializer,
    ItemEstoqueSerializer,
)
from inventory.models import ItemEstoque


class ViaturaViewSet(viewsets.ModelViewSet):
    queryset = Viatura.objects.all()
    serializer_class = ViaturaSerializer


class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer


class ManutencaoViewSet(viewsets.ModelViewSet):
    serializer_class = ManutencaoSerializer

    def get_queryset(self):
        queryset = Manutencao.objects.all()
        viatura_id = self.request.query_params.get("viatura")
        equipamento_id = self.request.query_params.get("equipamento")
        if viatura_id:
            queryset = queryset.filter(viatura_id=viatura_id)
        if equipamento_id:
            queryset = queryset.filter(equipamento_id=equipamento_id)
        return queryset


class ServicoRealizadoViewSet(viewsets.ModelViewSet):
    serializer_class = ServicoRealizadoSerializer

    def get_queryset(self):
        queryset = ServicoRealizado.objects.all()
        viatura_id = self.request.query_params.get("viatura")
        equipamento_id = self.request.query_params.get("equipamento")
        if viatura_id:
            queryset = queryset.filter(viatura_id=viatura_id)
        if equipamento_id:
            queryset = queryset.filter(equipamento_id=equipamento_id)
        return queryset


class ItemEstoqueViewSet(viewsets.ModelViewSet):
    queryset = ItemEstoque.objects.all()
    serializer_class = ItemEstoqueSerializer
