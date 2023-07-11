from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Veda index<h2> <a href='https://vegamovies.party/'>Vega</a>")
def about(request):
    return HttpResponse("Veda about")