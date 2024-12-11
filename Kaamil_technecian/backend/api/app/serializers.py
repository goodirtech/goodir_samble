from rest_framework import serializers
from .models import *

# class StatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Status
#         fields = ['id', 'name', 'description']

class JobCategoryserializer(serializers.ModelSerializer):
    class Meta:
        model=JobCategory
        fields="__all__"

class VillageSerializer(serializers.ModelSerializer):
    # This will show the customer distribution by listing all customers linked to each village
    # customers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Village
        fields = ['id', 'name', 'description', "status"]


class Technitianserializer(serializers.ModelSerializer):
    job_role= serializers.PrimaryKeyRelatedField(queryset=JobCategory.objects.all())
    # job_id=serializers.PrimaryKeyRelatedField(queryset=JobCategory.objects.all(), source="job_role")
    address=serializers.PrimaryKeyRelatedField(queryset=Village.objects.all())
    class Meta:
        model=Technician
        fields = [
            "id",
            "name",
            "job_role",      
            "address",
            "phone_number",
            "status",
            "image"
        ]

class ClientSerializer(serializers.ModelSerializer):
    address=serializers.PrimaryKeyRelatedField(queryset=Village.objects.all())
    class Meta:
        model = Client
        fields = ['id', 'name', 'phone', 'address', "status", "description"]

class JobSerializer(serializers.ModelSerializer):
    job_category=serializers.PrimaryKeyRelatedField(queryset=JobCategory.objects.all())
    technician_name=serializers.PrimaryKeyRelatedField(queryset=Technician.objects.all())
    customer_address=serializers.PrimaryKeyRelatedField(queryset=Village.objects.all())
    # client_name=serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    class Meta:
        model = Job
        fields = [
            'id',
            'customer_name',
            'customer_phone',
            'customer_address',
            'job_category',
            'job_description',
            'technician_name',
            'total_cost',
            'technician_salary',
            "status",
            'created_at',
            'updated_at',
        ]
        

class ClientJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientJob
        fields = [
            'id', 'client', 'created_at', 'updated_at',  
             'job_category', 'job_description', 
            'technician_name', 'technician_salary','total_cost','status'
        ]
       
       