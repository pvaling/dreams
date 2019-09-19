from django.http import HttpResponse
from django.shortcuts import render

def landing(request):
    return render(request=request, template_name='core/landing.html', context={})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    a = 5

    extra = request.user

    # social_acc = request.user.socialaccount_set.first()
    #
    # if social_acc.provider == 'facebook':
    #     pic = f"http://graph.facebook.com/{social_acc.uid}/picture?type=square"
    # elif social_acc.provider == 'google':
    #     pic = social_acc.extra_data['picture']
    #

    return render(request=request, template_name='core/profile.html', context={
        'user': request.user,
        # 'pic': pic
    })
