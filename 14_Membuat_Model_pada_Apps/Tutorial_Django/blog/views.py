from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "halaman" : "Blog",
        "nama_website" : "Kelas Terbuka",
    }
    return render(request, "index.html", context)
