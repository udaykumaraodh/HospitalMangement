from rest_framework import serializers
from task.models import *


class SaleSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields='__all__'

class PreHospSerializer(serializers.ModelSerializer):
    class Meta:
        model=PreRegHos
        field='__all__'