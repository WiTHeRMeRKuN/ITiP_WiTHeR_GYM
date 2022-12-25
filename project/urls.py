from django.contrib import admin
from django.urls import path, include
from WiTHeR_GYM.views import *
from users.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Abonement', AbonementViewSet)
router.register(r'Client', ClientViewSet)
router.register(r'Employes', EmployesViewSet)
router.register(r'Premises', PremisesViewSet)
router.register(r'PriceList', PriceListViewSet)
router.register(r'SaleAbonements', SaleAbonementsViewSet)
router.register(r'Schedule', ScheduleViewSet)
router.register(r'Services', ServicesViewSet)
router.register(r'SpecEmployes', SpecEmployesViewSet)
router.register(r'TrackingVisits', TrackingVisitsViewSet)
router.register(r'TypesOfTraining', TypesOfTrainingViewSet)

wither_gym_urls = [
    path('WiTHeR_GYM_Base/', include(router.urls)),
]

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(wither_gym_urls)),
    path('login/', AuthorizationUserView.as_view(), name='login'),
    path('registr/', RegistrationUserView.as_view(), name='registr'),
]
