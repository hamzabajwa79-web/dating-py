from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Match, Block
from .serializers import MatchSerializer
from django.db.models import Q
from django.db import models


class MatchListView(generics.ListAPIView):
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]



    def get_queryset(self):
        user_profile = self.request.user.profile
        return Match.objects.filter(
            (models.Q(user1=user_profile) | models.Q(user2=user_profile)) &
            models.Q(is_active=True)
            
        )
    

api_view(['POST'])
permission_classes([IsAuthenticated])

def unmatch(request, match_id):
    try:
        match = Match.objects.get(id=match_id)
        if match.user1.user == request.user or match.user2.user == request.user:
            match.is_active = False
            match.save()
            return Response({'message': 'Unmatched successfully'})
        return Response({'error':  'NONE AUTHORIZE'}, status=403)
    except Match.DoesNotExist:
         return Response({'error': 'Match not found'}, status=404)

