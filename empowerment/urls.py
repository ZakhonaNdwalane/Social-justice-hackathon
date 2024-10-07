from django.urls import path
from . import views
from .views import home

app_name = 'empowerment'

# Add your URLs here

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
   
    # Add your other URLs here
    path('financial-services/', views.financial_services, name='financial_services'),
    path('job-listings/', views.job_listings, name='job_listings'),
    path('wealth-initiatives/', views.wealth_initiatives, name='wealth_initiatives'),
]

