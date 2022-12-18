from django.shortcuts import render
from .models import Post  # import class Post untuk akses data konten


# Create your views here.
def index(request):
    # inisialisasi class Post ke dalam suatu variabel
    posts = Post.objects.all()
    context = {
        "halaman" : "Blog",
        "nama_website" : "Kelas Terbuka",
        "Posts" : posts,
    }
    return render(request, "blog/index.html", context)
