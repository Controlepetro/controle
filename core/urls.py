from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fleet.views import ViaturaViewSet, EquipamentoViewSet, ManutencaoViewSet, ServicoRealizadoViewSet

router = DefaultRouter()
router.register(r"viaturas", ViaturaViewSet)
router.register(r"equipamentos", EquipamentoViewSet)
router.register(r"manutencoes", ManutencaoViewSet)
router.register(r"servicos", ServicoRealizadoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
