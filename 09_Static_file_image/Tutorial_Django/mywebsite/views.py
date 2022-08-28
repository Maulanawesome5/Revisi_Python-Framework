from django.shortcuts import render


# function views disini
def index(request):
    context = {
        "judul" : "Kelas Terbuka",
        "subjudul" : "Home",
        "nav" : [
            ["/", "Home"],
            ["/about", "About"],
            ["/blog", "Blog"],
        ],
        "banner" : "img/banner_home.png",
    }
    return render(request, "index.html", context)
