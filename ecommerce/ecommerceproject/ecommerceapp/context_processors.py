from .models import Category

def categorylinks(request):
    links=Category.objects.all()
    return dict(links=links)
