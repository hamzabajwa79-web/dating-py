from rest_framework import serializers
from .models import UserProfile, Swipe, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image', 'is_primary', 'uploaded_at']



class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source = 'user.email',read_only=True)
    username = serializers.CharField(source = 'user.username',read_only =True)
    photos = PhotoSerializer(many=True,read_only=True)
    distance = serializers.SerializerMethodField()




    class Meta:
        model = UserProfile
        fields = ['id','email', 'username', 'bio', 'location', 'gender', 'looking_for', 'age',
                  'profile_picture', 'interests', 'height', 'occupation', 'education', 'latitude',
                  'longitude', 'is_premium', 'last_active', 'photos', 'distance'
                  
                 ]    

    def get_distance(self,obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user_profile = request.user.profile
            if user_profile.latitude and user_profile.longitude and obj.latitude and obj.longitude:
                from math import radians, sin, cos, sqrt, atan2
                lat1,lon1 = radians(user_profile.latitude), radians(user_profile.longitude)
                lat2,lon2 = radians(obj.latitude),radians(obj.longitude)
                dlat = lat2 - lat1
                dlon = lon2 - lon1
                a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2   
                c = 2 * atan2(sqrt(a), sqrt(1-a))
                return round(6371 *c,1)
            return None


class SwipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swipe
        fields = ['id', 'swiper', 'swiped_on', 'swipe_type', 'created_at']    