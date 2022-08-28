from django.shortcuts import render


# buat function views disini
def index(request):
    context = {
        "title" : "Kelas Terbuka",
        "subtitle" : "Beranda",
        # dibawah ini adalah template tags
        "nav" : [
            ['/', "Home"],
            ['/blog/', "Blog"],
            ['/community/', "Community"],
            ['/profiles/', "Profiles"],
        ],
    }
    return render(request, "index.html", context)
