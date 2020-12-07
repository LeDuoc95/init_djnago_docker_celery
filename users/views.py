from rest_framework_simplejwt.views import TokenViewBase
from users.serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenViewBase):
    serializer_class = CustomTokenObtainPairSerializer