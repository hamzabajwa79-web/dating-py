from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import response
from django.db.models import Q
from .models import UserProfile, Photo, Swipe
from .serializers import UserProfileSerializer, SwipeSerializer, PhotoSerializer
from users.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile



class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
    
    
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        #full update profile.
        serializer = self.get_serializer(self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
        return response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        #partial profile update.
        serializer = self.get_serializer(self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
        return response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
    


api_view(['GET'])
permission_classes([IsAuthenticated])
def potential_matches(request):
    user_profile = request.user.profile


    swiped_user = Swipe.objects.filter(swiper = user_profile). values_list('swiped_on', many=True)

    potential_profiles = UserProfile.objects.filter(
        gender = user_profile.looking_for,
        looking_for = user_profile.gender
    ).exclude(

        Q(user=request.user) | Q(id__in=swiped_user)
              

    )

    serializer = UserProfileSerializer(
        potential_profiles,
        many=True,
        context = {'request': request}

    )

    return response(serializer.data)



api_view(['POST'])
permission_classes([IsAuthenticated])
def swipe(request, profile_id, action):
    try:

        target_profile = UserProfile.objects.get(id=profile_id) 
    except UserProfile.DoseNotExist:
        return response ({'error': 'profile not found'}, status=status.HTTP_404_NOT_FOUND  )
    
    user_profile = request.user.profile
    

    if Swipe.objects.filter(swiper=user_profile, swiped_on=target_profile).exists():
        return response({'error': 'Allerady swipe on this profile'}, status=status.HTTP_404_NOT_FOUND)
    

    swipe =  Swipe.objects.create(
        swiper = user_profile,
        swiped_on = target_profile,
        swipe_type = action

    )


    if action in ['like', 'super_like']:
    
    
        mutual_swipe = Swipe.objects.filter(
            swiper = target_profile,
            swiped_on = user_profile,
            swipe_type_in = ['like', 'super_like'] 
        ).first()



    if mutual_swipe:

        from matches.models import Match
        match = Match.objects.create(user1=user_profile, user2=target_profile)
        return response({
                'match': True,
                'match_id': match.id,
                'message': "It's a match!"
            })
    
    return response({'match': False, 'message': 'Swipe recorded'})    


        








