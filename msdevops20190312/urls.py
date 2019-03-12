from django.conf.urls import url
from django.contrib import admin

from django.http import HttpResponse
def root(request):
    return HttpResponse('Hello World')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', root),
]
