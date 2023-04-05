from django.shortcuts import render
from rest_framework import viewsets, status, filters
from . models import Health_Test_Result
from . serializers import HealthTestResultSerializer

# Create your views here.
class HealthTestResultViewset(viewsets.ModelViewSet):
    queryset = Health_Test_Result.objects.all()
    serializer_class = HealthTestResultSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    filter_backends = [
        # DjangoFilterBackend,
        # filters.SearchFilter,
        # filters.OrderingFilter,
    ]
    # filterset_class = ProductFilter
    # permission_classes = [IsAuthenticated]
    parser_classes = [
        # MultiPartParser,
    ]
    search_fields = [
        "name",
        "cost_price",
        "selling_price",
        "current_quantity",
        "default_quantity",
        "minimum_stock_quantity",
        "category__name",
        "unit_type__name",
    ]
    ordering_fields = ["name", "quantity", "selling_price", "cost_price"]

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = ProductInventory.objects.filter(created_by=user)
    #     if self.action == "customers":
    #         return OrderItem.objects.filter(created_by=user)
    #     if "ADMIN" in user.roles:
    #         queryset = super().get_queryset()
    #     return queryset

