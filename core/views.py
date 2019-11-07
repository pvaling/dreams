import json

from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


@transaction.atomic()
@csrf_exempt
def firebase(request):
    import pyrebase

    user_token = json.loads(request.body)['token']
    # decoded_token = auth.verify_id_token(id_token)
    # uid = decoded_token['uid']

    config = {
        "apiKey": "AIzaSyCWReDq8-b9ZXygPaWix9bF1TM4jeI9f5k",
        "authDomain": "AIzaSyCWReDq8-b9ZXygPaWix9bF1TM4jeI9f5k",
        "databaseURL": "https://dreams-e1e71.firebaseio.com",
        "storageBucket": "",
        "serviceAccount": "dreams/dreams-e1e71-firebase-adminsdk-5sro8-0a4d20b707.json"
    }

    firebase = pyrebase.initialize_app(config)

    resp = firebase.auth().get_account_info(id_token=user_token)

    user_ext_id = resp['users'][0]['localId']
    phone = resp['users'][0].get('phoneNumber')

    user_exists = User.objects.filter(username=user_ext_id).count()

    if not user_exists:
        user = User.objects.create(username=user_ext_id, is_active=True)
    else:
        user = User.objects.get(username=user_ext_id)

    if Token.objects.filter(user=user).count():
        token = Token.objects.get(user=user)
    else:
        token = Token.objects.create(user=user)

    return JsonResponse({'token': token.key})


def landing(request):
    return render(request=request, template_name='core/landing.html', context={})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def profile(request):
    return render(request=request, template_name='core/profile.html', context={
        'user': request.user
    })

