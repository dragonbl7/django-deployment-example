from django.contrib import admin
from my_app1.models import AccessRecord, Topic, Webpage, Users, Signup, UserProfileInfo
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Users)
admin.site.register(Signup)
admin.site.register(UserProfileInfo)