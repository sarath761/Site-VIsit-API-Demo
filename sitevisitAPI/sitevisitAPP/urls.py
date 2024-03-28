from django.urls import path
from . import views


urlpatterns = [

    path('', views.UserLoginAPIView.as_view(), name='user-login'),
    
    path('ClientDetails/', views.Client_Details_API.as_view(), name='Client_Details_API'),#This creates the sitevisit instance for seperate creation
    path('ClientDetails/<int:pk>/', views.Client_Details_API.as_view(), name='Client_Details_API'),
    


    path('BasicDetailsSiteVisit/', views.Basic_Details_SiteVisit.as_view(), name='BasicDetailsSiteVisit'),#This creates the sitevisit instance for seperate creation
    path('BasicDetailsSiteVisit/<int:pk>/', views.Basic_Details_SiteVisit.as_view(), name='BasicDetailsSiteVisit'),
    
    path('Image_Seperate_Creation/', views.Image_Seperate_Creation.as_view(), name='ImageSeperateCreation'),#This creates the SiteVisitImage instance for seperate creation
    path('Image_Seperate_Creation/<int:pk>/', views.Image_Seperate_Creation.as_view(), name='ImageSeperateCreation'),
    #path("add",views.add_person),
    #path("show",views.get_all_records),
    path('ChecklistItemSeperateCreation/', views.ChecklistItem_Seperate_Creation.as_view(), name='ChecklistItemSeperateCreation'),#This creates the SiteVisitChecklistItem instance for seperate creation
    path('ChecklistItemSeperateCreation/<int:pk>/', views.ChecklistItem_Seperate_Creation.as_view(), name='ChecklistItemSeperateCreation'),

]
#image_type json
"""{
        "id": 96,
        "created_by": {
            "id": 2,
            "username": "sarath"
        },
        "created_date": "2024-03-25T13:29:42.259398Z",
        "updated_date": "2024-03-25T13:29:42.259404Z",
        "visit": "ptm",
        
        "_id": "66017c46f868036b41afc5db",
        "item_type": "section",
        "title": "any title",
        "items": [
            {
                "item_type": "description",
                "descrition": "abcdefg...."
            }
        ],




        
        
}"""



{
  'id': 96,
  'created_by': {'id': 2, 'username': 'sarath'},
  'created_date': 'datetime.datetime(2024, 3, 25, 13, 29, 42, 259398, tzinfo=datetime.timezone.utc)',
  'updated_date': 'datetime.datetime(2024, 3, 25, 13, 29, 42, 259404, tzinfo=datetime.timezone.utc)',
        'visit': 'ptm', 
        '_id': '66017c46f868036b41afc5db', 
        'item_type': 'section', 
        'title': 'any title', 
        'items': [
            {
                'item_type': 'description', 
                'descrition': 'abcdefg....'
            }
            ]
}