from django.shortcuts import render


# buat views function disini
def index(request):
    return render(request, template_name="index.html")
