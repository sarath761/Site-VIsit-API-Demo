
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class SiteVisit(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    #delete_status = models.PositiveSmallIntegerField(default=0)
    visit = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    plan_file = models.FileField(upload_to='site_visit_plans/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Completed', 'Completed')], blank=True, null=True)
    
    def __str__(self):
        return self.visit


class SiteVisitPhoto(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    #delete_status = models.PositiveSmallIntegerField(default=0)
    id = models.AutoField(primary_key=True)
    visit = models.ForeignKey(SiteVisit, on_delete=models.CASCADE)
    images = models.FileField(upload_to='site_visit_photos/',null=True,blank=True,default='')
    tag = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"site {self.images} for visit {self.visit.id}"
    



class ChecklistItem(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    #delete_status = models.PositiveSmallIntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    visit = models.ForeignKey(SiteVisit, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"ID:{self.id} and Task {self.task} for visit {self.visit.id}"
