from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지 알아내고
    page = request.GET.get('page')
    #request도니 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request,'blog/home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog_detail})   

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))    

def blogpost(request):
    #1.입력된 내용 처리 -> POST
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

        #2.빈 페이지를 띄워주는 기능 -> GET        
    else:
        form = BlogPost()
        return render(request, 'blog/new.html', {'form':form})
        