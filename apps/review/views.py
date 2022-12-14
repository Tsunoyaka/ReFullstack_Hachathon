from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from rest_framework.views import APIView
from .serializers import LikeSerializer, DislikeSerializer

from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from .serializers import CommentCRUDSerializer, CommentDelUpdSerializer, CommentSerializerSet
from .models import Comment
from .permissions import IsOwner
from apps.hotel.models import Hotel


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerSet

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context  


# class CreateCommentView(APIView):
#     permission_classes = [IsAuthenticated]
#     @swagger_auto_schema(request_body=CommentCRUDSerializer)
#     def post(self, request: Request):
#         serializer = CommentCRUDSerializer(data=request.data,  context={'request': request})
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user)
#             return Response('Comment Created!')


# class DesUpdCommentView(APIView):
#     permission_classes = [IsAdminUser, IsOwner]



#     def delete(self, request, pk):
#         obj = Comment.objects.get(pk=pk)
#         serializer = CommentDelUpdSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid(raise_exception=True):
#             serializer.delete()
#             return Response('Comment deleted!')

#     @swagger_auto_schema(request_body=CommentDelUpdSerializer)
#     def put(self, request, pk):
#         try:
#             instance = Comment.objects.get(pk=pk)
#             serailizer = CommentDelUpdSerializer(data=request.data, instance=instance, context={'request': request})
#             if serailizer.is_valid(raise_exception=True):            
#                 serailizer.save()  
#             return Response('?????????????????????? ?????????????? ??????????????')
#         except Comment.DoesNotExist:
#             return Response('???????????????? ???? ??????????????!', status=status.HTTP_404_NOT_FOUND)


class LikeView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(request_body=LikeSerializer)
    def post(self, request, pk):
        serializer = LikeSerializer(data=request.data,  context={'request': request, 'pk': pk})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response('???? ?????????????????? ?????????????? "????????????????!"')

    @swagger_auto_schema(request_body=LikeSerializer)
    def delete(self, request, pk):
        serializer = LikeSerializer(data=request.data,  context={'request': request, 'pk': pk})
        if serializer.is_valid(raise_exception=True):
            serializer.unlike()
            return Response('???? ???????????? ?????????????? "????????????????!"')


class DislikeView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(request_body=DislikeSerializer)
    def post(self, request, pk):
        serializer = DislikeSerializer(data=request.data,  context={'request': request, 'pk': pk})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response('???? ?????????????????? ?????????????? "???? ????????????????!"')

    @swagger_auto_schema(request_body=DislikeSerializer)
    def delete(self, request, pk):
        serializer = DislikeSerializer(data=request.data,  context={'request': request, 'pk': pk})
        if serializer.is_valid(raise_exception=True):
            serializer.undislike()
            return Response('???? ???????????? ?????????????? "???? ????????????????!"')

