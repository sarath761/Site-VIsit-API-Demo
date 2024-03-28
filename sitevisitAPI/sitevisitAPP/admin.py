from django.contrib import admin
from .models import SiteVisit,SiteVisitPhoto,ChecklistItem,ClientDetails

# Register your models
admin.site.register(SiteVisit)
admin.site.register(SiteVisitPhoto)
admin.site.register(ClientDetails)
admin.site.register(ChecklistItem)

