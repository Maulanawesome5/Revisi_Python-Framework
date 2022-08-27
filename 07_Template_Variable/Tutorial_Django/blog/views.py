from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "judul" : "Kelas Terbuka",
        "section" : "Blog",
        "contributor" : "Mario Ucup",
    }
    return render(request, template_name="blog/index.html", context=context)

def news(request):
    context = {
        "judul" : "Kelas Terbuka",
        "section" : "News",
        "contributor" : "Otong Surotong",
    }
    return render(request, template_name="blog/index.html", context=context)

def cerita(request):
    context = {
        "judul" : "Kelas Terbuka",
        "section" : "Cerita",
        "contributor" : "Sandra Bulog",
    }
    return render(request, template_name="blog/index.html", context=context)
