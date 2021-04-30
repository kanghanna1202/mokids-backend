from rest_framework import serializers

from user.models import User


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            nickname=validated_data['nickname']
        )
        user.set_password(validated_data['password'])

        user.save()
        return user
