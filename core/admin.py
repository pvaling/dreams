from django.contrib import admin

# Register your models here.
from core.models import Dream, Vote, Donation, Video, Profile

admin.site.register(Dream)
admin.site.register(Vote)
admin.site.register(Donation)
admin.site.register(Video)
admin.site.register(Profile)
