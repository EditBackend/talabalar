from rest_framework.routers import DefaultRouter
from .views import TalabaViewSet,GuruhViewSet,TolovViewSet,TolovQaytarishViewSet

router = DefaultRouter()
router.register('talabalar', TalabaViewSet)
router.register('guruhlar', GuruhViewSet)
router.register('tolovlar', TolovViewSet)
router.register('refundlar', TolovQaytarishViewSet)

urlpatterns = router.urls
