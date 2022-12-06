from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    UserRegistrationSerializer, 
    PasswordChangeSerializer,
    RestorePasswordSerializer,
    SetRestoredPasswordSerializer,
    UsersSerializer
    )


User = get_user_model()




class UserView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk):
        """
        Return a list of all users.
        """
        user = User.objects.get(email=pk)
        serializer = UsersSerializer(instance=user)
        # # usernames = [user.username for user in User.objects.all()]
        return Response(serializer.data)

class ListUsersView(APIView):
    def get(self, request):
        usernames = User.objects.all()
        list_ = []
        for user in usernames:
           B = {
            'user': user.username,
            'email': user.email 
           }
           list_.append(B)
        return Response(list_)
        # emails = [user.email for user in User.objects.all()]


class RegistrationView(APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request: Request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Thanks for registration! Activate your account via link in your mail',
                status=status.HTTP_201_CREATED
            )

class AccountActivationView(APIView):
    def get(self, request, activation_code):
        user = User.objects.filter(activation_code=activation_code).first()
        if not user:
            return Response(
                'PaGenrege not found', 
                status=status.HTTP_404_NOT_FOUND
                )
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response(
            'Account activated! You can login now', 
            status=status.HTTP_200_OK
            )


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Password changed succesfully',
                status=status.HTTP_200_OK
            )


class RestorePasswordView(APIView):
    def post(self, request: Request):
        serializer = RestorePasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_code()
            return Response(
                'Code was sent to your email',
                status=status.HTTP_200_OK
            )


class SetRestoredPasswordView(APIView):
    def post(self, request: Request):
        serializer = SetRestoredPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Password restored successfully',
                status=status.HTTP_200_OK
            )


class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request):
        username = request.user.username
        User.objects.get(username=username).delete()
        return Response(
            'Account deleted successfully',
            status=status.HTTP_204_NO_CONTENT
        )

