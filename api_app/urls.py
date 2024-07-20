from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import HouseViewSet, ApartmentViewSet, TariffViewSet, WaterMeterViewSet, WaterMeterReadingViewSet, \
    CalculatePaymentView, CheckPaymentCalculationProgress

router = DefaultRouter()
router.register(r'tariffs', TariffViewSet, basename='tariffs')
router.register(r'houses', HouseViewSet, basename='houses')
router.register(r'apartments', ApartmentViewSet, basename='apartments')
router.register(r'water_meters', WaterMeterViewSet, basename='water_meters')
router.register(r'water_meter_readings', WaterMeterReadingViewSet, basename='water_meter_readings')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('calculate-payment/', CalculatePaymentView.as_view()),
    path('payment-calculation-progress/<str:task_id>/', CheckPaymentCalculationProgress.as_view(), name='payment-calculation-progress'),
]