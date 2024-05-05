from rest_framework import serializers
from .models import User, Doctor, Nurse, Patient, Appointment, Medicine, Prescription, Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'name', 'specialization']

class NurseSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Nurse
        fields = ['id', 'user', 'name']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['id', 'user', 'name', 'date_of_birth', 'address']

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'time', 'status']

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'description']

class PrescriptionSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer()
    medicine = MedicineSerializer()

    class Meta:
        model = Prescription
        fields = ['id', 'appointment', 'medicine', 'dosage', 'instructions']

class PaymentSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer()

    class Meta:
        model = Payment
        fields = ['id', 'appointment', 'amount', 'payment_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Patient
        fields = ('id', 'user', 'name', 'date_of_birth', 'address')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Patient.objects.create(user=user, **validated_data)

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Doctor
        fields = ('id', 'user', 'name', 'specialization')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Doctor.objects.create(user=user, **validated_data)

class NurseSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Nurse
        fields = ('id', 'user', 'name')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Nurse.objects.create(user=user, **validated_data)