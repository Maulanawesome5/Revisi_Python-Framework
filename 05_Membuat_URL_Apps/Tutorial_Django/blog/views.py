from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, template_name="blog.html")

def recent_post(request):
    titles = "<h1>Halaman Recent Post</h1>"
    subtitles = "<h2>Berada di dalam Halaman Blog</h2>"
    page_link = """
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
            <ul>
                <li><a href="/blog/recent">Recent Post</a></li>
            </ul>
            <li><a href="/about/">About</a></li>
        </ul>
    """

    output_text = titles + subtitles + page_link

    return HttpResponse(content=output_text)
    # return HttpResponse(content=output_text)
