from django.contrib import admin
from .models import SiteVisit,SiteVisitPhoto,ChecklistItem

# Register your models
admin.site.register(SiteVisit)
admin.site.register(SiteVisitPhoto)
#admin.site.register(ImageTag)
admin.site.register(ChecklistItem)

