from django.shortcuts import render
from .models import FinancialService, JobListing, WealthInitiatives
# Create your views here.

def home(request):
    return render(request, 'empowerment/home.html') 

def financial_services(request):
    services = FinancialService.objects.all()
    return render(request, 'empowerment/financial_services.html', {'services': services})

def job_listings(request):
    jobs = JobListing.objects.all()
    return render(request, 'empowerment/job_listings.html', {'jobs': jobs})

def wealth_initiatives(request):
    initiatives = WealthInitiatives.objects.all()
    return render(request, 'empowerment/wealth_initiatives.html', {'initiatives': initiatives})

