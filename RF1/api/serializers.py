from rest_framework import serializers
from Data.models import Fac
class FacSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fac
        fields="__all__"
        
        