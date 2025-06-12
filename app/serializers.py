from rest_framework import serializers
from app.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'role', 'phone_number', 'email', 'language', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        user = User(
            role=validated_data['role'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            language=validated_data['language']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user