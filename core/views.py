from django.http import HttpResponse
from django.shortcuts import render

def landing(request):
    return HttpResponse("Landing")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    a = 5

    extra = request.user
    pic = request.user.socialaccount_set.first().extra_data['picture']
    return render(request=request, template_name='core/profile.html', context={
        'user': request.user,
        'pic': pic
    })
