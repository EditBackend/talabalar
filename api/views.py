from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import TolovQaytarish, Talaba, Guruh, Tolov, SMS
from .serializers import TolovQaytarishSerializer,TalabaSerializer,GuruhSerializer,TolovSerializer




class TolovQaytarishViewSet(ModelViewSet):
    queryset = TolovQaytarish.objects.all()
    serializer_class = TolovQaytarishSerializer

    def perform_create(self, serializer):
        refund = serializer.save()

        tolov = refund.tolov
        talaba = tolov.talaba

        # Balansdan ayirish
        talaba.balans -= refund.miqdor
        talaba.save()



class TalabaViewSet(ModelViewSet):
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer

    @action(detail=True, methods=['post'])
    def sms_yuborish(self, request, pk=None):
        talaba = self.get_object()
        matn = request.data.get('matn')

        SMS.objects.create(
            talaba=talaba,
            matn=matn
        )

        return Response(
            {"xabar": "SMS muvaffaqiyatli yuborildi"},
            status=status.HTTP_200_OK
        )


class GuruhViewSet(ModelViewSet):
    queryset = Guruh.objects.all()
    serializer_class = GuruhSerializer



class TolovViewSet(ModelViewSet):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializer

    def perform_create(self, serializer):
        tolov = serializer.save()


        talaba = tolov.talaba
        talaba.balans += tolov.miqdor
        talaba.save()

