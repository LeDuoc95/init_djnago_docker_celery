from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import datetime
from users.models import User


class CustomTokenObtainPairSerializer(TokenObtainSerializer):

    def __init__(self, *args, **kwargs):
        if 'email' in kwargs['data']:
            self.username_field = 'email'
        super().__init__(*args, **kwargs)

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        self.user.last_login = datetime.datetime.now()

        self.user.save()

        return data