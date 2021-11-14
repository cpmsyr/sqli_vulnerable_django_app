from django.contrib import admin
from django.urls import path
from vulnerable_app.views import parts, searchparts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('searchparts/', searchparts),
    path('parts/', parts)
]
