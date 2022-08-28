from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "judul" : "Kelas Terbuka",
        "subjudul" : "Blog",
        "nav" : [
            ["/", "Home"],
            ["/about", "About"],
            ["/blog", "Blog"],
        ],
        "banner" : "blog/img/banner_blog.png",
    }
    return render(request, "blog/index.html", context)
