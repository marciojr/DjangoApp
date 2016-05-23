from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def auth(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('blog.post_list.html'))
            else:
                return render("Ciclista Desabilitado")
        return render(request, 'blog/post_list.html', {"Usuario ou senha invalido."})
	