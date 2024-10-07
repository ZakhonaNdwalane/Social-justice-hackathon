from django.urls import path
from . import views
from .views import home, contact, financial_services, job_listings, wealth_initiatives, signup_view, login_view, logout_view

app_name = 'empowerment'

urlpatterns = [
    # Main page
    path('', home, name='home'),
    
    # Contact page
    path('contact/', contact, name='contact'),
    
    # Authentication routes
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    
    # Additional services and initiatives
    path('financial-services/', financial_services, name='financial_services'),
    path('job-listings/', job_listings, name='job_listings'),
    path('wealth-initiatives/', wealth_initiatives, name='wealth_initiatives'),
    
]
