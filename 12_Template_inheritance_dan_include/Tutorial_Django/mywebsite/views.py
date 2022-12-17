from django.shortcuts import render


def index(request):
    context = {
        'banner' : 'img/banner_home.png',
        'favicon' : 'img/favicon.png',
        'halaman' : 'Home',
        'judul' : 'Kelas Terbuka',
        'subjudul' : 'Selamat Datang',
    }
    return render(request, 'index.html', context)