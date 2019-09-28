from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from moneyed import Money
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, authentication_classes
from rest_framework.viewsets import ModelViewSet

from core.models import Dream, Vote, Donation
from rest_api.serializers.dream import DreamSerializer


class DreamViewSet(ModelViewSet):
    """
        A viewset for viewing and editing dream instances.
        """
    serializer_class = DreamSerializer
    queryset = Dream.objects.all()
    authentication_classes = [TokenAuthentication]

    @staticmethod
    def make_vote(pk, user, vote):
        dream = Dream.objects.get(pk=int(pk))
        Vote.objects.create(value=vote, author=user, content_object=dream)

    @login_required
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        self.make_vote(pk=pk, user=request.user, vote=Vote.POSITIVE)
        return JsonResponse({'result': 'ok'})


    @login_required
    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        self.make_vote(pk=pk, user=request.user, vote=Vote.NEGATIVE)
        return JsonResponse({'result': 'ok'})


    # @login_required
    @action(detail=True, methods=['post'])
    def donate(self, request, pk=None):
        dream = Dream.objects.get(pk=int(pk))
        try:
            donation = Donation(
                author=request.user,
                purpose=dream,
                amount=Money(amount=1.5, currency='USD')
            )
            donation.save()
            # dream.donation_set.create(author=request.user, amount=1.5)
        except Exception as e:
            a=5

        return JsonResponse({'result': 'ok'})


