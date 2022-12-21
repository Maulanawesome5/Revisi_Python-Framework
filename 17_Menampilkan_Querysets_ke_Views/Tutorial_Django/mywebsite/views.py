from django.shortcuts import render


def index(request):
    context = {
        "halaman" : "Beranda",
        "website" : "Kelas Terbuka",
    }
    return render(request, "index.html", context)
