from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from new_app.forms import BloggerForm
from new_app.models import Blogger


# Create your views here.
def home(request):
    query = request.GET.get('q','')
    blogger = Blogger.objects.all()
    if query:
        blogger = blogger.filter(
            Q(name__icontains=query) | Q(phone__icontains=query)
        )

    paginator = Paginator(blogger, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html' , {"page_obj": page_obj, 'query':query })


def register(request):
    form = BloggerForm()
    if request.method == 'POST':
        form1 = BloggerForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/')

    return render(request, 'register.html', {'form' : form})