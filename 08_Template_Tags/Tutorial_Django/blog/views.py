from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "title" : "Kelas Terbuka",
        "subtitle" : "Blog",
        # dibawah ini adalah template tags
        "nav" : [
            ['/', "Home"],
            ['/blog/', "Blog"],
            ['/community/', "Community"],
            ['/profiles/', "Profiles"],
        ],
    }
    return render(request, "blog/index.html", context)
