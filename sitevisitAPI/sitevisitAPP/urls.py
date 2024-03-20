from django.urls import path
from . import views


urlpatterns = [

    path('', views.UserLoginAPIView.as_view(), name='user-login'),
    
    path('BasicDetailsSiteVisit/', views.Basic_Details_SiteVisit.as_view(), name='BasicDetailsSiteVisit'),#This creates the sitevisit instance for seperate creation
    path('BasicDetailsSiteVisit/<int:pk>/', views.Basic_Details_SiteVisit.as_view(), name='BasicDetailsSiteVisit'),
    
    path('Image_Seperate_Creation/', views.Image_Seperate_Creation.as_view(), name='ImageSeperateCreation'),#This creates the SiteVisitImage instance for seperate creation
    path('Image_Seperate_Creation/<int:pk>/', views.Image_Seperate_Creation.as_view(), name='ImageSeperateCreation'),
    
    path('ChecklistItemSeperateCreation/', views.ChecklistItem_Seperate_Creation.as_view(), name='ChecklistItemSeperateCreation'),#This creates the SiteVisitChecklistItem instance for seperate creation
    path('ChecklistItemSeperateCreation/<int:pk>/', views.ChecklistItem_Seperate_Creation.as_view(), name='ChecklistItemSeperateCreation'),

]

