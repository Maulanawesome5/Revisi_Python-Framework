from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "judul" : "Kelas Terbuka",
        "subjudul" : "Blog",
        "_" : "_",
    }
    return render(request, "index.html", context)
