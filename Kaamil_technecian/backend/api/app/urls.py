from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView,TokenBlacklistView,
)

urlpatterns=[
    path('technicians/', views.TechnicianListCreateView.as_view(), name='technician-list-create'),
    path('technicians/<int:pk>/', views.TechnicianRetrieveUpdateDestroyView.as_view(), name='technician-detail'),

    # Job Category URLs
    path('job_categories/', views.jobCategoryListCreateView.as_view(), name='jobcategory-list-create'),
    path('job_categories/<int:pk>/', views.jobCategoryRetrieveUpdateDestroyView.as_view(), name='jobcategory-detail'),
    # Village URLs
    path('villages/', views.VillageListCreateView.as_view(), name='village-list-create'),
    path('villages/<int:pk>/', views.VillageRetrieveUpdateDestroyView.as_view(), name='village-detail'),
    
    path('jobs/', views.JobListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', views.JobRetrieveUpdateDestroyView.as_view(), name='job-detail'),

     # client URLs
    path('clients/', views.ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    # status URLs
    # path('statuses/', views.StatusListCreateView.as_view(), name='status-list-create'),
    # path('statuses/<int:pk>/', views.StatusDetailView.as_view(), name='status-detail'),

    path('client-jobs/', views.ClientJobListCreateView.as_view(), name='clientjob-list-create'),
    path('client-jobs/<int:pk>/', views.ClientJobRetrieveUpdateDestroyView.as_view(), name='clientjob-detail'),
    #authentication
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),  # <- This line includes Djoser's JWT URLs
    path('auth/jwt/logout',TokenBlacklistView.as_view(), name="logout")
]