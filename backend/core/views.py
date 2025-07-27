from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from core.permissions import IsAdminUserCustom, IsResidentUserCustom
from rest_framework.permissions import IsAuthenticated

# Home API (just for testing)
@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to Society Management API!"})

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role', 'resident')  # default to resident

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    if CustomUser.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = CustomUser.objects.create_user(username=username, password=password, role=role)

    # ✅ Generate JWT token immediately after registration
    refresh = RefreshToken.for_user(user)

    return Response({
        'message': f'{role.capitalize()} registered successfully',
        'user': {
            'username': user.username,
            'role': user.role
        },
        'tokens': {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    }, status=status.HTTP_201_CREATED)



# Example: Admin-only
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUserCustom])
def update_society_info(request):
    return Response({"message": "Society info updated successfully (dummy response)"})

# Resident-only
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsResidentUserCustom])
def my_dues(request):
    return Response({"dues": 1200, "status": "pending"})
