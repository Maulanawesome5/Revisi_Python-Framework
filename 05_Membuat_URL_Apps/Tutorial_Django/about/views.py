from django.shortcuts import render


# Create your views here
def index(request):
    return render(request, template_name="about.html")

def about_me(request):
    return render(request, template_name="about_me.html")
