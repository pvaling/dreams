from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    a = 5
    return render(request=request, template_name='core/profile.html', context={
        'user': request.user
    })
