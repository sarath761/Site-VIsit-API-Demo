from .serializers import UserSerializer,ChecklistItemSerializer,SiteVisitPhotoSerializer,BasicDetailsSerializer,Image_Seperate_Serializer,ChecklistItem_Seperate_Serializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import SiteVisit, SiteVisitPhoto,ChecklistItem

#User Login and Token Generation
class UserLoginAPIView(APIView):
    #authentication_classes = (JWTAuthentication) 
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user using provided credentials
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



#This creates the sitevisit instance for seperate creation
class Basic_Details_SiteVisit(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, format=None):
        serializer = BasicDetailsSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            user_id = request.user.id
            serializer.validated_data['created_by_id'] = user_id
            serializer.save() 
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None, format=None):
        if pk is not None:
            site_visit = SiteVisit.objects.get(pk=pk, created_by=request.user)
            serializer = BasicDetailsSerializer(site_visit)
            return Response(serializer.data)
        else:
            site_visits = SiteVisit.objects.filter(created_by=request.user)
            serializer = BasicDetailsSerializer(site_visits, many=True)
            return Response(serializer.data)


    def put(self, request, pk, format=None):
        try:
            site_visit = SiteVisit.objects.get(pk=pk)
            
        except SiteVisit.DoesNotExist:
            return Response({'error': 'Site visit not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BasicDetailsSerializer(site_visit, data=request.data, partial=True) 
        
        if serializer.is_valid(): 
                    
            serializer.save()
              
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        try:
            site_visit = SiteVisit.objects.get(pk=pk)
            site_visit.delete()
            return Response({'Success': 'Site visit Deleted'},status=status.HTTP_200_OK)
        except SiteVisit.DoesNotExist:
            return Response({'error': 'Site visit not found'}, status=status.HTTP_404_NOT_FOUND)

    


#This creates the SiteVisitImage instance for seperate creation
class Image_Seperate_Creation(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    

    def post(self, request, format=None):
        serializer = Image_Seperate_Serializer(data=request.data, context={'request': request})  
             
        if serializer.is_valid():
            serializer.save() 
            #print(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request,  pk=None,format=None):
        
        if pk is not None:  # If pk is provided in the request
            try:
                photo = SiteVisitPhoto.objects.get(pk=pk)  # Retrieve specific SiteVisitPhoto instance
                serializer = Image_Seperate_Serializer(photo)  # Serialize the instance
                return Response(serializer.data)  # Return serialized data as a response
            except SiteVisitPhoto.DoesNotExist:
                return Response({"error": "SiteVisitPhoto does not exist."}, status=status.HTTP_404_NOT_FOUND)
        else:  # If no pk provided, return all instances for the current user and visit
            photos = SiteVisitPhoto.objects.filter(visit__created_by=request.user)  # Filter by user
            serializer = Image_Seperate_Serializer(photos, many=True)  # Serialize instances
            return Response(serializer.data)  # Return serialized data as a response
    

    def put(self, request, pk, format=None):
        try:
            photo = SiteVisitPhoto.objects.get(pk=pk)
        except SiteVisitPhoto.DoesNotExist:
            return Response({"error": "SiteVisitPhoto does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Image_Seperate_Serializer(photo, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        try:
            photo = SiteVisitPhoto.objects.get(pk=pk)
        except SiteVisitPhoto.DoesNotExist:
            return Response({"error": "SiteVisitPhoto does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        photo.delete()
        return Response({'Success': 'Photo Instance Deleted'},status=status.HTTP_204_NO_CONTENT)



#This creates the SiteVisitChecklistItem instance for seperate creation
class ChecklistItem_Seperate_Creation(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, format=None):
        serializer = ChecklistItem_Seperate_Serializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            user_id = request.user.id
            serializer.validated_data['created_by_id'] = user_id
            created_instance=serializer.save() 
            return Response({'id': created_instance.id, 'Success': 'ChecklistItem_Created'},status=status.HTTP_201_CREATED)
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                checklist = ChecklistItem.objects.get(pk=pk)
            except ChecklistItem.DoesNotExist:
                return Response({"error": "ChecklistItem does not exist"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ChecklistItem_Seperate_Serializer(checklist)
            return Response(serializer.data)
        else:
            checklist = ChecklistItem.objects.filter(created_by=request.user)
            serializer = ChecklistItem_Seperate_Serializer(checklist, many=True)
            return Response(serializer.data)
    
    

    def put(self, request, pk, format=None):
        try:
            instance = ChecklistItem.objects.get(pk=pk)
        except ChecklistItem.DoesNotExist:
            return Response({"error": "ChecklistItem does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ChecklistItem_Seperate_Serializer(instance, data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            instance = ChecklistItem.objects.get(pk=pk)
        except ChecklistItem.DoesNotExist:
            return Response({"error": "ChecklistItem does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({'Success': 'CheckList Item Deleted'},status=status.HTTP_200_OK)
   



#All in one creation of sitevist
"""class createSitevisitAPI(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, format=None):
        serializer = SiteVisitSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            user_id = request.user.id
            serializer.validated_data['created_by_id'] = user_id
            created_instance = serializer.save() 
            return Response({'id': created_instance.id, 'Success': 'Site visit Created'},status=status.HTTP_201_CREATED)
            #return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, pk=None, format=None):
        if pk is not None:
            site_visit = SiteVisit.objects.prefetch_related('images__tags').get(pk=pk, created_by=request.user)
            serializer = SiteVisitSerializer(site_visit)
            return Response(serializer.data)
        else:
            site_visits = SiteVisit.objects.prefetch_related('images__tags').filter(created_by=request.user)
            serializer = SiteVisitSerializer(site_visits, many=True)
            return Response(serializer.data)
        
    def delete(self, request, pk, format=None):
        try:
            site_visit = SiteVisit.objects.get(pk=pk)
            site_visit.delete()
            return Response({'Success': 'Site visit Deleted'},status=status.HTTP_200_OK)
        except SiteVisit.DoesNotExist:
            return Response({'error': 'Site visit not found'}, status=status.HTTP_404_NOT_FOUND)
"""




