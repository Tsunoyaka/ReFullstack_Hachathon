from django.urls import path

from .views import  DislikeView, LikeView, CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('crud', CommentViewSet, 'comcrud')


urlpatterns = [
    # path('add-comment/', CreateCommentView.as_view(), name='create_com'),
    # path('upd-del-comment/<int:pk>/', DesUpdCommentView.as_view()),
    path('like/<str:pk>/', LikeView.as_view()),
    path('dislike/<str:pk>/', DislikeView.as_view()),
]

urlpatterns += router.urls