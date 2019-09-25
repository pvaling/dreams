from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.models import Dream, Vote
from rest_api.serializers.dream import DreamSerializer


class DreamViewSet(ModelViewSet):
    """
        A viewset for viewing and editing dream instances.
        """
    serializer_class = DreamSerializer
    queryset = Dream.objects.all()


    @login_required
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        dream = Dream.objects.get(pk=int(pk))
        Vote.objects.create(value=Vote.POSITIVE, author=request.user, content_object=dream)
