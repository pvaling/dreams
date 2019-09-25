import copy
import uuid

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from core.models import Video, Dream, Profile


def index(request):
    return HttpResponse("Index")


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def feed(request):

    # current_user_id = 3
    # print(request.headers)
    # print(request.user)

    dreams = Dream.objects.exclude(
        author=request.user,
        author__profile__isnull=True
    ).filter(active=True).all()

    feed_data = []

    for dream in dreams:
        try:
            feed_data.append(
                {
                    "id": dream.id,
                    "name": dream.author.profile.display_name,
                    "budget": str(dream.budget),
                    "country": dream.author.profile.country.name,
                    "status": 'Online' if dream.author.profile.get_presence_status else 'Offline',
                    "match": str(dream.get_progress),
                    "description": dream.author.profile.description,
                    "message": dream.description,
                    "label": dream.title,
                    "image":
                        dream.author.profile.avatar.url
                        if dream.author.profile.avatar
                        else 'https://dreams-videos.s3.eu-central-1.amazonaws.com/02.jpg',
                    "video": dream.media.file.url
                }
            )
        except Exception as e:
            print("Something wrong with dream: {dream}".format(dream=dream))

    return JsonResponse(feed_data, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):

    profile = Profile.objects.get(user=request.user)

    feed_data = {
     "id": request.user.id,
     "name": profile.display_name,
     "match": '27',
     "description": profile.description,
     "status": profile.get_presence_status,
     "message": "It's not who I am underneath but what I do that defines me.",
     "image": profile.avatar.url if profile.avatar else None
    }

    return JsonResponse(feed_data)


def my_dream(request):

    dream_data = {
     "id": 5,
     "name": 'Petr Valing',
     "match": '27',
     "description": 'Software developer, Wakeboarder, Musician. Dreaming about Norway yacht trip',
     "status": 'Offline',
     "message": "It's not who I am underneath but what I do that defines me.",
     "image": 'https://dreams-videos.s3.eu-central-1.amazonaws.com/11.jpg',
     "video": 'https://dreams-videos.s3.eu-central-1.amazonaws.com/IMG_0891_comressed.mp4'
    }

    return JsonResponse(dream_data)



from django import forms


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def upload_file(request):
    if request.method == 'POST':

        user_id = request.user.id

        form_data = copy.deepcopy(request.POST)
        form_data['author'] = user_id
        request.FILES['file'].name = str(user_id) + '.mp4'
        form = UploadFileForm(form_data, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return JsonResponse({"ok": True})
        except Exception as e:
            return JsonResponse({"ok": False})
    else:
        return JsonResponse({"ok": False})
