from rest_framework import serializers
from .models import Viatura, Equipamento, Manutencao, ServicoRealizado, AplicacaoItem
from inventory.models import ItemEstoque


class ItemEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemEstoque
        fields = "__all__"


class AplicacaoItemSerializer(serializers.ModelSerializer):
    item = ItemEstoqueSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=ItemEstoque.objects.all(), source="item", write_only=True
    )

    class Meta:
        model = AplicacaoItem
        fields = ["id", "item", "item_id", "quantidade", "liberado_por"]


class ManutencaoSerializer(serializers.ModelSerializer):
    itens = AplicacaoItemSerializer(many=True, required=False)

    class Meta:
        model = Manutencao
        fields = ["id", "viatura", "equipamento", "data", "descricao", "motivo", "usuario", "itens"]

    def create(self, validated_data):
        itens_data = validated_data.pop("itens", [])
        manutencao = Manutencao.objects.create(**validated_data)
        for item_data in itens_data:
            AplicacaoItem.objects.create(manutencao=manutencao, **item_data)
        return manutencao


class ServicoRealizadoSerializer(serializers.ModelSerializer):
    itens = AplicacaoItemSerializer(many=True, required=False)

    class Meta:
        model = ServicoRealizado
        fields = ["id", "viatura", "equipamento", "data", "descricao", "observacoes", "usuario", "itens"]

    def create(self, validated_data):
        itens_data = validated_data.pop("itens", [])
        servico = ServicoRealizado.objects.create(**validated_data)
        for item_data in itens_data:
            AplicacaoItem.objects.create(servico=servico, **item_data)
        return servico


class ViaturaSerializer(serializers.ModelSerializer):
    manutencoes = ManutencaoSerializer(many=True, read_only=True)
    servicos = ServicoRealizadoSerializer(many=True, read_only=True)

    class Meta:
        model = Viatura
        fields = ["id", "placa", "modelo", "ano", "status", "odometro", "manutencoes", "servicos"]


class EquipamentoSerializer(serializers.ModelSerializer):
    manutencoes = ManutencaoSerializer(many=True, read_only=True)
    servicos = ServicoRealizadoSerializer(many=True, read_only=True)

    class Meta:
        model = Equipamento
        fields = ["id", "numero_serie", "tipo", "horas_trabalhadas", "status", "manutencoes", "servicos"]
