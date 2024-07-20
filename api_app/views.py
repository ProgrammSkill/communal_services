from rest_framework import viewsets, status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from api_app.models import House, Apartment, Tariff, WaterMeter, WaterMeterReadings
from api_app.serializers import HouseSerializer, ApartmentSerializer, TariffSerializer, WaterMeterReadingsSerializer, \
    WaterMeterSerializer, PaymentSerializer
from api_app.swagger_content import house, apartment, tariff, water_meter, water_meter_reading, calculate_payment_in_house
from .task import calculate_payment


@tariff
class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


@house
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all().prefetch_related('apartments')
    serializer_class = HouseSerializer


@apartment
class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.prefetch_related('water_meters__readings').select_related('house').all()
    serializer_class = ApartmentSerializer


@water_meter
class WaterMeterViewSet(viewsets.ModelViewSet):
    queryset = WaterMeter.objects.select_related('apartment').prefetch_related('readings').all()
    serializer_class = WaterMeterSerializer


@water_meter_reading
class WaterMeterReadingViewSet(viewsets.ModelViewSet):
    queryset = WaterMeterReadings.objects.select_related('water_meter__apartment').all()
    serializer_class = WaterMeterReadingsSerializer


@calculate_payment_in_house
class CalculatePaymentView(CreateAPIView):
    serializer_class = PaymentSerializer

    def post(self, request,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        calculate_payment.delay(request.data)
        return Response({'message': 'Расчёт кварплаты рассчитан'}, status=status.HTTP_201_CREATED)


@calculate_payment_in_house
class CheckPaymentCalculationProgress(generics.ListAPIView):

    def list(self, request, **kwargs):
        task_id = self.kwargs.get('task_id')
        print(task_id)
        task = calculate_payment.AsyncResult(task_id)
        if task.state == 'PENDING':
            response = {
                'state': task.state,
                'status': 'Pending...'
            }
        elif task.state != 'FAILURE':
            response = {
                'state': task.state,
                'status': task.info.get('status', '')
            }
        else:
            response = {
                'state': task.state,
                'status': str(task.info)
            }
        return Response(response)
