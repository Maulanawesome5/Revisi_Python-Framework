from django.shortcuts import render


# function views disini
def index(request):
    context = {
        "judul" : "Kelas Terbuka",
        "subjudul" : "Home",
        "_" : "_",
    }
    return render(request, "index.html", context)
