from rest_framework import serializers
from .models import User, Password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("داداش کمتر از ۸ کاراکتر نمیشع ")
        return value


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        exclude = ['user']
