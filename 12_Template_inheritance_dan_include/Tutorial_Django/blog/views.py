from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "app_css" : "blog/css/styles.css",
        "banner" : "blog/img/banner_blog.png",
        "halaman" : "Blog",
        "judul" : "Kelas Terbuka",
        "subjudul" : "Selamat Datang",
    }
    return render(request, "blog/index.html", context)
