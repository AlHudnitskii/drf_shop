from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from apps.users.models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
   email = request.data.get('email')
   password = request.data.get('password')
   
   if not email or not password:
      pass
   