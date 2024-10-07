from django.shortcuts import render, redirect, get_object_or_404
from .models import FinancialService, JobListing, WealthInitiatives
from django.utils import timezone
from datetime import datetime
from datetime import date
from django.db.models import Sum
from django.contrib import messages
from .forms import CreateInitiativeForm

# Create your views here.

# Home View
def home(request):
    return render(request, 'empowerment/home.html')

# Contact View
def contact(request):
    return render(request, 'empowerment/contact.html')

# Financial Services View
def financial_services(request):
    # Predefined list of important financial services for economic empowerment
    services = [
        FinancialService(
            name="Microloans",
            description="Small loans designed for individuals or small businesses, helping them start or expand.",
            eligibility_criteria="Low-income individuals, small business owners.",
            service_type="Loan",
            contact_info="contact@empowermentapp.com"
        ),
        FinancialService(
            name="Financial Literacy Programs",
            description="Workshops and courses to teach budgeting, saving, and investing.",
            eligibility_criteria="Open to all community members.",
            service_type="Education",
            contact_info="education@empowermentapp.com"
        ),
        FinancialService(
            name="Savings Programs",
            description="High-interest savings accounts and matched savings incentives to encourage saving.",
            eligibility_criteria="Open to individuals with savings goals.",
            service_type="Savings",
            contact_info="savings@empowermentapp.com"
        ),
        FinancialService(
            name="Insurance Products",
            description="Affordable insurance tailored for low-income individuals and small businesses.",
            eligibility_criteria="Individuals and small business owners.",
            service_type="Insurance",
            contact_info="insurance@empowermentapp.com"
        ),
        FinancialService(
            name="Investment Opportunities",
            description="Platforms for community members to invest in local businesses and projects.",
            eligibility_criteria="Open to all community members interested in investing.",
            service_type="Investment",
            contact_info="invest@empowermentapp.com"
        ),
        FinancialService(
            name="Expense Tracking Tools",
            description="Tools to help users track spending and analyze financial habits.",
            eligibility_criteria="All community members.",
            service_type="Financial Tool",
            contact_info="tracking@empowermentapp.com"
        ),
        FinancialService(
            name="Peer-to-Peer Lending",
            description="Connects lenders and borrowers within the community.",
            eligibility_criteria="Community members.",
            service_type="Loan",
            contact_info="lending@empowermentapp.com"
        ),
    ]

    return render(request, 'empowerment/financial_services.html', {'services': services})

# Job Listings View
def job_listings(request):
    # Predefined list of job opportunities for economic empowerment
    jobs = [
        JobListing(
            title="Sales Associate",
            description="Looking for a friendly and motivated sales associate to join our retail team.",
            company="XYZ Retailers",
            location="Downtown",
            salary=30000.00,  # Example salary
            posted_at="2024-10-01"
        ),
        JobListing(
            title="Electrician",
            description="Seeking a licensed electrician for residential and commercial projects.",
            company="ABC Electrical Services",
            location="Citywide",
            salary=50000.00,
            posted_at="2024-09-25"
        ),
        JobListing(
            title="Marketing Intern",
            description="Gain hands-on experience in digital marketing and social media management.",
            company="Tech Innovations",
            location="Remote",
            salary=15000.00,
            posted_at="2024-09-20"
        ),
        JobListing(
            title="Freelance Graphic Designer",
            description="Looking for creative individuals to design marketing materials and social media posts.",
            company="Freelance Network",
            location="Remote",
            salary=20000.00,
            posted_at="2024-09-15"
        ),
        JobListing(
            title="Customer Service Representative",
            description="Provide excellent customer service and customer experience to our customers.",
            company="ABC Bank",
            location="Downtown",
            salary=25000.00,
            posted_at="2024-09-10",
        ),
    ]

    return render(request, 'empowerment/job_listings.html', {'jobs': jobs})

# Wealth Initiatives View
def wealth_initiatives(request):
    # Retrieve ongoing initiatives and all initiatives
    ongoing_initiatives = WealthInitiatives.objects.filter(end_date__gte=date.today())
    initiatives = WealthInitiatives.objects.all()

    # Calculate total stats
    total_funds_raised = sum(initiative.funds_raised for initiative in initiatives)
    total_beneficiaries = sum(int(initiative.beneficiaries) for initiative in initiatives)

    # Initialize the form outside of the request method check
    form = CreateInitiativeForm()  # Default form initialization for GET request

    # Handle the form submission for creating, updating, or deleting an initiative
    if request.method == 'POST':
        if 'update_initiative' in request.POST:
            initiative_id = request.POST.get('initiative_id')
            initiative = get_object_or_404(WealthInitiatives, id=initiative_id)
            form = CreateInitiativeForm(request.POST, instance=initiative)
            if form.is_valid():
                form.save()
                messages.success(request, 'Initiative updated successfully.')
                return redirect('empowerment:wealth_initiatives')  # Redirect after POST
            else:
                messages.error(request, 'Failed to update initiative. Please check the form and try again.')
        elif 'delete_initiative' in request.POST:
            initiative_id = request.POST.get('initiative_id')
            initiative = get_object_or_404(WealthInitiatives, id=initiative_id)
            initiative.delete()
            messages.success(request, 'Initiative deleted successfully.')
            return redirect('empowerment:wealth_initiatives')  # Redirect after POST
        else:  # For creating a new initiative
            form = CreateInitiativeForm(request.POST)
            if form.is_valid():
                initiative = form.save(commit=False)
                initiative.save()
                messages.success(request, 'Initiative created successfully.')
                return redirect('empowerment:wealth_initiatives')  # Redirect after POST
            else:
                messages.error(request, 'Failed to create initiative. Please check the form and try again.')
    else:
        form = CreateInitiativeForm()  # Initialize the form for GET requests

    # Pass the data to the template
    context = {
        'form': form,
        'ongoing_initiatives': ongoing_initiatives,
        'initiatives': initiatives,
        'total_funds_raised': total_funds_raised,
        'total_beneficiaries': total_beneficiaries,
    }

    return render(request, 'empowerment/wealth_initiatives.html', context)

