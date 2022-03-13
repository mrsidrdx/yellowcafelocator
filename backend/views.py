from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from django.contrib.auth import login
from knox.models import AuthToken
from .serializers import LoginUserSerializer, UserSerializer, ListUserLocationsSerializer, CreateUserLocationsSerializer
from .models import UserLocations

# Create your views here

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        }, status=200)

# Show user last 10 locations

class UserLocationsListAPI(generics.ListCreateAPIView):
    model = UserLocations
    permission_classes = [permissions.IsAuthenticated,]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserLocationsSerializer
        return ListUserLocationsSerializer

    def get_queryset(self):
        user = self.request.user
        return UserLocations.objects.filter(user=user).order_by('-timestamp')[:10]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        location = UserLocations.objects.create(
            user=request.user,
            latitude=serializer.data['latitude'],
            longitude=serializer.data['longitude'])

        result = ListUserLocationsSerializer(location)
        return Response(result.data, status=status.HTTP_201_CREATED)