from django.contrib.auth.models import User

from rest_framework import serializers



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        username = validated_data['username']
        user = User(username=username)
        user.set_password(validated_data['password'])
        user.save()
        return user