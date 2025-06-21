from django.shortcuts import render, redirect

from new_app.forms import BloggerForm
from new_app.models import Blogger


# Create your views here.
def home(request):
    blogger = Blogger.objects.all()
    return render(request, 'home.html' , {"blogger": blogger})


def register(request):
    form = BloggerForm()
    if request.method == 'POST':
        form1 = BloggerForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/')

    return render(request, 'register.html', {'form' : form})