from rest_framework import serializers
from .models import Health_Test_Result


class HealthTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Test_Result
        fields = "__all__"
        # extra_kwargs = {
        #     "id": {"read_only": True},
        # }
        # ordering = ("name",)
