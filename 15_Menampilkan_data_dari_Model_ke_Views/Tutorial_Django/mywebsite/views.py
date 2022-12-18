from django.shortcuts import render


def index(request):
    context = {
        "halaman" : "Home",
        "nama_website" : "Kelas Terbuka",
    }
    return render(request, "index.html", context)
