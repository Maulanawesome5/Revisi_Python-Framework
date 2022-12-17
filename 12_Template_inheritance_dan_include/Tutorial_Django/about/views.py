from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "app_css" : "about/css/styles.css",
        "banner" : "about/img/banner_about.png",
        "halaman" : "About",
        "judul" : "Kelas Terbuka",
        "subjudul" : "Selamat Datang",
    }
    return render(request, "about/index.html", context)
