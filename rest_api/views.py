from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Index")


def feed(request):
    feed_data = [
    {
     "id": 1,
     "name": 'Leanne Graham',
     "status": 'Online',
     "match": '78',
     "description": 'Full-time Traveller. Globe Trotter. Occasional Photographer. Part time Singer/Dancer.',
     "message": 'I will go back to Gotham and I will fight men Iike this but I will not become an executioner.',
     "image": '../images/01.jpg',
     "video": 'https://dreams-videos.s3.eu-central-1.amazonaws.com/preroll.mp4'
    },
    {
     "id": 5,
     "name": 'Petr Valing',
     "match": '27',
     "description":'Software developer, Wakeboarder, Musician. Dreaming about Norway yacht trip',
     "status": 'Offline',
     "message": "It's not who I am underneath but what I do that defines me.",
     "image": '../images/11.jpg',
     "video": 'https://dreams-videos.s3.eu-central-1.amazonaws.com/IMG_0891_comressed.mp4'
    },
    {
     "id": 2,
     "name": 'Clementine Bauch',
     "match": '93',
     "description":'Full-time Traveller. Globe Trotter. Occasional Photographer. Part time Singer/Dancer.',
     "status": 'Offline',
     "message": "Someone like you. Someone who'll rattle the cages.",
     "image": '../images/02.jpg'
    }
    ]

    return JsonResponse(feed_data, safe=False)
