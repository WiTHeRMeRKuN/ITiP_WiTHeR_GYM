from rest_framework import viewsets
from .serializers import *

class AbonementViewSet(viewsets.ModelViewSet):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class EmployesViewSet(viewsets.ModelViewSet):
    queryset = Employes.objects.all()
    serializer_class = EmployesSerializer

class PremisesViewSet(viewsets.ModelViewSet):
    queryset = Premises.objects.all()
    serializer_class = PremisesSerializer

class PriceListViewSet(viewsets.ModelViewSet):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer

class SaleAbonementsViewSet(viewsets.ModelViewSet):
    queryset = SaleAbonements.objects.all()
    serializer_class = SaleAbonementsSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class SpecEmployesViewSet(viewsets.ModelViewSet):
    queryset = SpecEmployes.objects.all()
    serializer_class = SpecEmployesSerializer

class TrackingVisitsViewSet(viewsets.ModelViewSet):
    queryset = TrackingVisits.objects.all()
    serializer_class = TrackingVisitsSerializer

class TypesOfTrainingViewSet(viewsets.ModelViewSet):
    queryset = TypesOfTraining.objects.all()
    serializer_class = TypesOfTrainingSerializer