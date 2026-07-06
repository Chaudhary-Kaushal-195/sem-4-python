from rest_framework.routers import DefaultRouter
from api.views import facviewset

router = DefaultRouter()
router.register(r,'fac',facviewset,basename='player')
urlpatterns = router.urls
