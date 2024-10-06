from django.contrib import admin
from .models import FinancialService, JobListing, WealthDistributionInitiative

# Register your models here.

admin.site.register(FinancialService)
admin.site.register(JobListing)
admin.site.register(WealthDistributionInitiative)

