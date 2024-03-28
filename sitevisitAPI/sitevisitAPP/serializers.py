from rest_framework import serializers
from .models import SiteVisit, SiteVisitPhoto,ChecklistItem,ClientDetails
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']



class Client_Details_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_date=serializers.DateTimeField(read_only=True)
    client_name = serializers.CharField(max_length=100)
    client_mob_num = serializers.CharField()
    country_code = serializers.CharField()
    category=serializers.CharField(max_length=50)
    location = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=100)
    
    
    
    def create(self, validated_data):
        return ClientDetails.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.client_name = validated_data.get('client_name', instance.client_name)
        instance.client_mob_num = validated_data.get('client_mob_num', instance.client_mob_num)
        instance.country_code = validated_data.get('country_code', instance.country_code)
        instance.location = validated_data.get('location', instance.location)
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


#This creates the sitevisit instance for seperate creation
class BasicDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_by = UserSerializer(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    visit = serializers.CharField(max_length=100)
   
    
    def create(self, validated_data):
        
        validated_data['created_by'] = self.context['request'].user
        
        sitevisit_data = {
            'created_by' : validated_data['created_by'],
            'visit': validated_data['visit'],   
        }
        sitevisit = SiteVisit.objects.create(**sitevisit_data)

        return sitevisit

    def update(self, instance, validated_data):
        # Update the instance fields with validated data
        instance.visit = validated_data.get('visit', instance.visit)
        # Save the updated instance
        instance.save()
        return instance
  
    

#This creates the SiteVisitImage instance for seperate creation
class Image_Seperate_Serializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SiteVisitPhoto
        fields = ['id', 'created_date', 'visit', 'images', 'tag']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None  # Get the current user from the request
        
        images = validated_data.pop('images')
        tag = validated_data.pop('tag')
        visit = validated_data.pop('visit')
        
        created_instance = SiteVisitPhoto.objects.create(
            visit=visit, images=images, tag=tag, created_by=user
        )
        
        return created_instance

    def update(self, instance, validated_data):
        instance.images = validated_data.get('images', instance.images)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.save()
        return instance



class ChecklistItem_Seperate_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = ChecklistItem
        fields = ['id', 'created_date', 'visit', 'task', 'completed', 'notes']
        
    def create(self, validated_data):
        # Extract visit from validated data
        visit = validated_data.pop("visit")
        
        # Set created_by to the current user
        validated_data['created_by'] = self.context['request'].user
        
        # Create the checklist item
        checklist_item = ChecklistItem.objects.create(visit=visit, **validated_data)

        return checklist_item
    
    def update(self, instance, validated_data):
        # Update the instance fields with validated data
        instance.visit = validated_data.get('visit', instance.visit)
        instance.task = validated_data.get('task', instance.task)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.notes = validated_data.get('notes', instance.notes)

        # Save the updated instance
        instance.save()
        return instance