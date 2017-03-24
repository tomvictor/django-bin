#api views
from MainApp.models import Post
from MainApp.api.serializers import MsgListSerializer,MsgDetailSerializer,MsgCreateSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )

class MsgCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = MsgCreateSerializer


class MsgListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = MsgListSerializer


class MsgDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = MsgDetailSerializer

class MsgUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = MsgDetailSerializer


class MsgDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = MsgDetailSerializer

