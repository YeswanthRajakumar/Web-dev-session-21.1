
from django.urls import path
from django.urls.conf import include
from django.http import HttpResponse

def getHello(request):
    return HttpResponse("Hello Protosem")



urlpatterns = [
    path('', getHello ),
]
