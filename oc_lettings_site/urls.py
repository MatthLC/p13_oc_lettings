from django.contrib import admin
from django.urls import path, include

from . import views

from django.urls import path


def trigger_error(request):
    return division_by_zero = 1 / 0

def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('sentry-debug/', trigger_error),
]
