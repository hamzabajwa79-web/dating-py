from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)

    class Meta:
        model = CustomUser
        fields = ('email','username','password','password2','date_of_birth')


    def validate(self, attrs):
      if attrs['password'] != attrs['password2']:
        raise serializers.ValidationError({
            'password2': "Passwords don't match"
        })
      return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user
    


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username = email , password = password)
            if not user:
                raise serializers.ValidationError('invalid cardinate')
            attrs['user'] = user
            return attrs
        raise serializers.ValidationError('email and Password is required')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','username','date_of_birth','is_verified','created_at')
