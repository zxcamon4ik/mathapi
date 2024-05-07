from django.http import HttpResponse, HttpRequest


async def index(request):
    return HttpResponse("hello world!")
