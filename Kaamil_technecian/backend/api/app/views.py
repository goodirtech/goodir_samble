from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django.db.models import ProtectedError
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ProtectedDeleteMixin:
    """
    A mixin to catch ProtectedError on delete and return a response with details
    about related objects that prevent deletion.
    """
    def delete(self, request, *args, **kwargs):
            try:
                # Attempt to delete the object
                return self.destroy(request, *args, **kwargs)
            except ProtectedError:
                # Retrieve the object instance
                instance = self.get_object()
                # Set the status to "inactive" (you can define the specific value in your model)
                instance.status = 'inactive'  # Adjust the status field and value as needed
                instance.save()

                return Response(
                    {
                        "message": "This item has been marked as inactive due to related dependencies.",

                    },
                    status=status.HTTP_200_OK, 
                )

# List and Create
class TechnicianListCreateView(generics.ListCreateAPIView):
    queryset = Technician.objects.all()
    serializer_class = Technitianserializer

# Retrieve, Update, and Delete
class TechnicianRetrieveUpdateDestroyView(ProtectedDeleteMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Technician.objects.all()
    serializer_class = Technitianserializer

# List and Create
class jobCategoryListCreateView(generics.ListCreateAPIView):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategoryserializer   

    

# Retrieve, Update, and Delete
class jobCategoryRetrieveUpdateDestroyView(ProtectedDeleteMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategoryserializer
    
   

# List and Create Villages
class VillageListCreateView(generics.ListCreateAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

# Retrieve, Update, and Delete Village
class VillageRetrieveUpdateDestroyView(ProtectedDeleteMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
 
    
    

# List and Create Jobs
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# Retrieve, Update, and Delete a Job
class JobRetrieveUpdateDestroyView(ProtectedDeleteMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# List and Create View
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Retrieve, Update, and Delete View
class ClientDetailView(ProtectedDeleteMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# List all statuses or create a new status
# class StatusListCreateView(generics.ListCreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# # Retrieve, update, or delete a specific status by ID
# class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

class ClientJobListCreateView(generics.ListCreateAPIView):
    queryset = ClientJob.objects.all()
    serializer_class = ClientJobSerializer

class ClientJobRetrieveUpdateDestroyView(ProtectedDeleteMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientJob.objects.all()
    serializer_class = ClientJobSerializer



