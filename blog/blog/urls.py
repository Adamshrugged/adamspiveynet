from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members/', include('django.contrib.auth.urls')),      # order of operations important - this is for user logins etc
    path('members/', include('members.urls')),                  # Other pages that are set up for members
]
