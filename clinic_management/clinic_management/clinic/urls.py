from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'nurses', views.NurseViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'medicines', views.MedicineViewSet)
router.register(r'prescriptions', views.PrescriptionViewSet)
router.register(r'payments', views.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]