from django.shortcuts import render, redirect, get_object_or_404
from .models import FinancialService, JobListing, WealthInitiatives
from django.utils import timezone
from datetime import date
from django.db.models import Sum
from django.contrib import messages
from .forms import CreateInitiativeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# Home View
@login_required
def home(request):
    return render(request, 'empowerment/home.html')

# Contact View
@login_required
def contact(request):
    return render(request, 'empowerment/contact.html')

# Financial Services View
@login_required 
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
@login_required
def wealth_initiatives(request):
    ongoing_initiatives = WealthInitiatives.objects.filter(end_date__gte=date.today())
    initiatives = WealthInitiatives.objects.all()
    total_funds_raised = initiatives.aggregate(Sum('funds_raised'))['funds_raised__sum']
    total_beneficiaries = initiatives.aggregate(Sum('beneficiaries'))['beneficiaries__sum']
    
    form = CreateInitiativeForm()  # Default form initialization for GET request

    if request.method == 'POST':
        if 'update_initiative' in request.POST:
            initiative_id = request.POST.get('initiative_id')
            initiative = get_object_or_404(WealthInitiatives, id=initiative_id)
            form = CreateInitiativeForm(request.POST, instance=initiative)
            if form.is_valid():
                form.save()
                messages.success(request, 'Initiative updated successfully.')
            else:
                messages.error(request, 'Failed to update initiative.')
        elif 'delete_initiative' in request.POST:
            initiative_id = request.POST.get('initiative_id')
            initiative = get_object_or_404(WealthInitiatives, id=initiative_id)
            initiative.delete()
            messages.success(request, 'Initiative deleted successfully.')
        else:
            form = CreateInitiativeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Initiative created successfully.')
            else:
                messages.error(request, 'Failed to create initiative.')
        return redirect('empowerment:wealth_initiatives')

    context = {
        'form': form,
        'ongoing_initiatives': ongoing_initiatives,
        'initiatives': initiatives,
        'total_funds_raised': total_funds_raised,
        'total_beneficiaries': total_beneficiaries,
    }

    return render(request, 'empowerment/wealth_initiatives.html', context)

#Login View
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}! You are now logged in.')
                return redirect('empowerment:home')  # Redirect after successful login
            else:
                messages.error(request, 'Invalid username or password. Redirecting to signup page.')
                return redirect('empowerment:signup')  # Redirect to the signup page if user is not found
        else:
            messages.error(request, 'Login form is invalid. Please check your inputs.')

    else:
        login_form = AuthenticationForm()  # Display empty form

    context = {
        'login_form': login_form,
    }
    return render(request, 'empowerment/login.html', context)

#Signup View
def signup_view(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('empowerment:login')  # Redirect to login page after signup
        else:
            messages.error(request, 'Signup form is invalid. Please check the information.')

    else:
        signup_form = UserCreationForm()  # Display empty form

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'empowerment/signup.html', context)

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('empowerment:login')