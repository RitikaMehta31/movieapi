from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	username=serializers.CharField(max_length=65,min_length=8)
	password=serializers.CharField(max_length=65,min_length=8,write_only=True)

	class Meta:
		model=User
		fields = ['username', 'password']

		def validate(self,attrs):
			if User.objects.filter(username=attrs['username']).exists():
				raise serializers.ValidationError({'username',('Username already exist')})
			return super().validate(attrs)

		def create(self, validated_data):
			return User.objects.create_user(**validated_data)


