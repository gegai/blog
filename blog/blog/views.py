from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from blog import models
from django.core.exceptions import ObjectDoesNotExist
from blog.forms import ArticleForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    contacts = models.Article.objects.all()
    paginator = Paginator(contacts, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'articles': articles})


def article_detail(request, article_id):
    try:
        article_obj = models.Article.objects.get(id=article_id)
    except ObjectDoesNotExist:
        return render(request, '404.html', {'err_msg': '该文章不存在'})
    return render(request, 'article.html', {'article_obj': article_obj})


def category(request, category_id):
    contacts = models.Article.objects.filter(category_id=category_id)
    paginator = Paginator(contacts, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'articles': articles})


def new_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            print('看我看我--->', request)
            form_data['author_id'] = request.user.id
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(request, 'new_article.html', {'new_article_obj': new_article_obj})
        else:
            print('error:', form.errors)
    category_list = models.Category.objects.all()
    return render(request, 'new_article.html', {'category_list': category_list})


def register(request):
    username = request.POST.get('user')
    password = request.POST.get('passwd')
    user = models.User.objects.create(username=username,
                               is_staff = True,
                               is_active = True)
    user.set_password(password)
    user.save()
    return HttpResponseRedirect('/log/')


def log(request):
    return render(request,'log.html')


def acc_login(request):
    err_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username,password=password)
        print('--------------->',user)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            err_msg = '错误的用户名或密码'
    return render(request,'log.html',{'err_msg':err_msg})


def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')