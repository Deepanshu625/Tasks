from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import TODO


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = ['id', 'title', 'details', 'user']

    user = serializers.SerializerMethodField('get_user')

    def get_user(self, obj):
        return obj.user.username

    def create(self, validated_data):
        validated_data['user'] = self.initial_data.get('user')
        return TODO.objects.create(**validated_data)
