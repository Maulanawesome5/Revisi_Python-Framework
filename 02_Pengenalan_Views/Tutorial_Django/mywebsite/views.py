from django.http import HttpResponse

# Membuat function di dalam file ini, file yang 
# ditampilkan di HTML

def index(request):
    title = "<h1> Halaman Beranda </h1>"
    subtitle = "<h2> Selamat datang di halaman beranda website </h2>"

    text_output = title + subtitle

    return HttpResponse(text_output)

def about(request):
    return HttpResponse("<h1> Halaman Tentang </h1>")
