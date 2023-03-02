"""Сериалайзеры приложения users."""
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей."""

    class Meta:
        """Мета класс пользователя."""

        fields = (
            'bio',
            'email',
            'first_name',
            'last_name',
            'role',
            'username'
        )
        model = User
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            ),
            EmailValidator,
            RegexValidator(
                regex=r'^[\w.@+-]',
                message='Недопустимый никнейм',
            )
        ]

    def validate_username(self, value):
        """Валидация имени пользователя."""
        if value == 'me':
            raise ValidationError('Имя пользователя "me" запрещено.')
        return value


class TokenSerializer(serializers.Serializer):
    """Сериализатор для токена."""

    username = serializers.CharField(max_length=150, required=True)

    class Meta:
        """Мета класс токена."""

        fields = '__all__'
        model = User


class MeSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя."""

    role = serializers.CharField(read_only=True)

    class Meta:
        """Мета класс пользователя."""

        model = User
        fields = (
            'bio',
            'email',
            'first_name',
            'last_name',
            'role',
            'username'
        )
