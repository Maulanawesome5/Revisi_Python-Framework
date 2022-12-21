from django.shortcuts import render
from .models import Articles

# Create your views here.
def index(request):
    article = Articles.objects.all()
    context = {
        "Articles" : article,
        "halaman" : "Blog",
        "kategori" : "All",
        "website" : "Kelas Terbuka",
    }
    return render(request, "index.html", context)

def jurnal(request):
    article = Articles.objects.filter(category="jurnal")
    context = {
        "Articles" : article,
        "halaman" : "Blog",
        "kategori" : "Jurnal",
        "website" : "Kelas Terbuka",
    }
    return render(request, "index.html", context)

def berita(request):
    article = Articles.objects.filter(category="berita")
    context = {
        "Articles" : article,
        "halaman" : "Blog",
        "kategori" : "Berita",
        "website" : "Kelas Terbuka",
    }
    return render(request, "index.html", context)

def gosip(request):
    article = Articles.objects.filter(category="gosip")
    context = {
        "Articles" : article,
        "halaman" : "Blog",
        "kategori" : "Gosip",
        "website" : "Kelas Terbuka",
    }
    return render(request, "index.html", context)

