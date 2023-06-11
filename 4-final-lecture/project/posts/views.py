from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostSerializer
from posts.permissions import IsAuthor


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['post'], detail=True, url_path='add-to-favorite',
            permission_classes=[IsAuthenticated],
            serializer_class=PostSerializer)
    def add_to_favorite(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.favorite_by.add(request.user)
        return Response({'status': 'OK'})
    
    @action(methods=['post'], detail=True, url_path='remove-from-favorite',
            permission_classes=[IsAuthenticated],
            serializer_class=PostSerializer)
    def remove_from_favorite(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.favorite_by.remove(request.user)
        return Response({'status': 'OK'})
    
    @action(methods=['post'], detail=True, url_path='toggle-favorite',
            permission_classes=[IsAuthenticated],
            serializer_class=PostSerializer)
    def toggle_favorite(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.favorite_by.filter(id=request.user.id).exists():
            obj.favorite_by.remove(request.user)
        else:
            obj.favorite_by.add(request.user)
        return Response(self.get_serializer(instance=obj).data)
