from rest_framework import serializers
from .models import Match, Block
from profiles.models import UserProfile
from profiles.serializers import UserProfileSerializer


class MatchSerializer(serializers.ModelSerializer):

    user1_detail = UserProfileSerializer(source='user1', read_only=True)
    user2_detail = UserProfileSerializer(source='user2', read_only=True)

    class Meta:
        model = Match
        fields  = ['id', 'user1', 'user2', 'created_at', 'is_active']