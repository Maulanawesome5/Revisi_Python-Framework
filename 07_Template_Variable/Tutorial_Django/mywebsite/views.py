from django.shortcuts import render


def index(request):
    # template variable
    context = {
        "judul" : "Kelas Terbuka",
        "contributor" : "Faqihza",
    }
    return render(request, template_name="index.html", context=context)
