from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Advertisement, AdvertisementStatusChoices, Favorite
from .serializers import AdvertisementSerializer, FavoriteSerializer
from .filters import AdvertisementFilter
from .permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
    
    def get_queryset(self):
        queryset = Advertisement.objects.all()
        if not self.request.user.is_authenticated:
            queryset = queryset.exclude(status=AdvertisementStatusChoices.DRAFT)
        else:
            queryset = queryset.filter(creator=self.request.user)
        return queryset
    
    @action(detail=True, methods=['post'])
    def add_to_favorites(self, request, pk=None):
        advertisement = self.get_object()
        if advertisement.creator == request.user:
            return Response({'error': 'You cannot add your own advertisement to favorites'})
        favorite = Favorite.objects.create(user=request.user, advertisement=advertisement)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def my_favorites(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        advertisements = [favorite.advertisement for favorite in favorites]
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data)

    
class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
