from django.http import HttpResponse
from django.shortcuts import render


# akan merender dokumen HTML
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    # return HttpResponse("<h1> Halaman About </h1>")
