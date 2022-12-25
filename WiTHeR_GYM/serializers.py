from rest_framework import serializers
from .models import *

class AbonementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonement
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class EmployesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employes
        fields = '__all__'

class PremisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premises
        fields = '__all__'

class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = '__all__'

class SaleAbonementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleAbonements
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class SpecEmployesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecEmployes
        fields = '__all__'

class TrackingVisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingVisits
        fields = '__all__'

class TypesOfTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesOfTraining
        fields = '__all__'
