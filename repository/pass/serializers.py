from rest_framework import serializers

from .models import User, Password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()

    def update(self, instance, validated_data):
        super().update(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("داداش کمتر از ۸ کاراکتر نمیشع ")
        return value


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        exclude = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
