from django.contrib import admin
from .models import FinancialService, JobListing, WealthInitiatives

# Register your models here.

admin.site.register(FinancialService)
admin.site.register(JobListing)
@admin.register(WealthInitiatives)
class WealthInitiativesAdmin(admin.ModelAdmin):
    list_display = ('initiative_name', 'funding_goal', 'funds_raised', 'start_date', 'end_date')
