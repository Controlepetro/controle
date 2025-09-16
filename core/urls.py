from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fleet.views import (
    ViaturaViewSet,
    EquipamentoViewSet,
    ManutencaoViewSet,
    ServicoRealizadoViewSet,
    ItemEstoqueViewSet,   # ✅ agora importado
)

# Cria o roteador da API
router = DefaultRouter()
router.register(r"viaturas", ViaturaViewSet)
router.register(r"equipamentos", EquipamentoViewSet)
router.register(r"manutencoes", ManutencaoViewSet)
router.register(r"servicos", ServicoRealizadoViewSet)
router.register(r"estoque", ItemEstoqueViewSet)   # ✅ rota do estoque

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # ✅ todas as rotas da API ficam em /api/
]
