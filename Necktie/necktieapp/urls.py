from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from necktieapp import views

router = DefaultRouter(trailing_slash=False)

router.register(r'doctors', views.DoctorViewset)
router.register(r'patients', views.PatientViewset)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
]