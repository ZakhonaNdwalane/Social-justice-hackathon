from django.urls import path
from . import views

urlpatterns = [
    path('financial-services/', views.financial_services, name='financial_services'),
    path('job-listings/', views.job_listings, name='job_listings'),
    path('wealth-initiatives/', views.wealth_initiatives, name='wealth_initiatives'),
]
