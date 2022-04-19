from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from app_sby.models import Category, Post, ImagePost, News, ImageNews, Feedback, Account

from .decorators import kiemtradangnhap, kiemtraquyenadmin
from .form import DangKy

# Trang quản trị


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_home(request):
    post_sl = Post.objects.count()
    news_sl = News.objects.count()
    feedback_sl = Feedback.objects.count()
    user_sl = User.objects.count()
    post = Post.objects.all().values('imagepost__link', 'title', 'prince', 'category__name')[:10]
    news = News.objects.all().values('imagenews__link', 'title', 'date_created')[:10]
    feedback = Feedback.objects.all().values('title', 'name')[:10]
    context = {
        'post_sl': post_sl,
        'news_sl': news_sl,
        'feedback_sl': feedback_sl,
        'user_sl': user_sl,
        'post': post,
        'news': news,
        'feedback': feedback
    }
    return render(request, 'root/index.html', context)


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_post_add(request):
    category_list = Category.objects.all()
    return render(request, 'root/post_add.html', {'category_list': category_list})


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_post_list(request):
    post = Post.objects.all().values('id', 'title', 'type', 'status', 'sold',
                                     'category', 'prince', 'date_created', 'category__name')
    return render(request, 'root/post_list.html', {'post': post})


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_post_add_process(request):
    if request.method == 'POST':
        title = request.POST['title']
        prince = request.POST['prince']
        address = request.POST['address']
        type = request.POST['radiothueban']
        description = request.POST['description']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        Post(title=title, prince=prince, address=address, type=type, category=category, description=description).save()
        lastpost = Post.objects.latest('id')
        link = request.FILES['image']
        ImagePost(link=link, post=lastpost).save()
    return root_post_list(request)


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_post_update_process(request, post_id):
    u = Post.objects.all().filter(id=post_id)
    category_list = Category.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        prince = request.POST['prince']
        address = request.POST['address']
        type = request.POST['radiothueban']
        description = request.POST['description']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        p = Post.objects.filter(id=post_id)
        p.update(title=title, prince=prince, address=address, type=type, category=category, description=description)
        if request.FILES.get('image', False):
            ImagePost.objects.filter(post=post_id).delete()
            link = request.FILES['image']
            i = Post.objects.get(pk=post_id)
            ImagePost(link=link, post=i).save()
        return root_post_list(request)
    return render(request, 'root/post_update.html', {'u': u, 'category_list': category_list})


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_post_delete_process(request, post_id):
    Post.objects.filter(id=post_id).delete()
    return root_post_list(request)


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_category(request):
    category_list = Category.objects.all()
    return render(request, 'root/category.html', {'category_list': category_list})


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_category_add(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        Category(name=name).save()
    return render(request, 'root/category.html', {'category_list': category_list})


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_category_update(request, category_id):
    category_list = Category.objects.all()
    category_update = Category.objects.filter(id=category_id)
    if request.method == 'POST':
        name = request.POST['name']
        t = Category.objects.filter(id=category_id)
        t.update(name=name)
        return root_category(request)
    return render(request, 'root/category_update.html', {'category_list': category_list,
                                                         'category_update': category_update})


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_category_delete(request, category_id):
    Category.objects.filter(id=category_id).delete()
    return root_category(request)


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_news(request):
    news_list = News.objects.all()
    return render(request, 'root/news_list.html', {'news_list': news_list})


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_news_add(request):
    return render(request, 'root/news_add.html')


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_news_add_process(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['description']
        News(title=title, content=content).save()
        lastnews = News.objects.latest('id')
        link = request.FILES['image']
        ImageNews(link=link, news=lastnews).save()
    return root_news(request)


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_news_update_process(request, news_id):
    u = News.objects.all().filter(id=news_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        n = News.objects.filter(id=news_id)
        n.update(title=title, content=description)
        if request.FILES.get('image', False):
            ImageNews.objects.filter(news=news_id).delete()
            link = request.FILES['image']
            i = News.objects.get(pk=news_id)
            ImageNews(link=link, news=i).save()
        return root_news(request)
    return render(request, 'root/news_update.html', {'u': u})


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_news_delete(request, news_id):
    News.objects.filter(id=news_id).delete()
    return root_news(request)


@login_required(login_url='dangnhap')
@kiemtraquyenadmin
def root_feedback(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'root/feedback.html', {'feedback_list': feedback_list})


def base(request):
    navbar = Category.objects.all()
    return navbar


def home(request):
    return render(request, 'user/trangchu.html', {'navbar': base(request)})


def private(request):
    return render(request, 'user/rieng-tu.html', {'navbar': base(request)})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['title']
        content = request.POST['content']
        Feedback(name=name, email=email, title=title, content=content).save()
    return render(request, 'user/lienhe.html', {'navbar': base(request)})


def about(request):
    return render(request, 'user/gioithieu.html', {'navbar': base(request)})


def doitac(request):
    return render(request, 'user/doi-tac-kinh-doanh.html', {'navbar': base(request)})


@kiemtradangnhap
def dangnhap(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'user/dangnhap.html', {'navbar': base(request)})


@kiemtradangnhap
def dangky(request):
    form = DangKy()
    if request.method == 'POST':
        form = DangKy(request.POST)
        if form.is_valid():
            user = form.save()
            user_id = User.objects.latest('id')
            Account(user_id=user_id).save()
            return redirect('dangnhap')
    return render(request, 'user/dangky.html', {'navbar': base(request), 'form': form})


def dangxuat(request):
    logout(request)
    return redirect('home')


def taikhoan(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_detail = Account.objects.get(user_id=user_id)
        return render(request, 'user/taikhoan2.html', {'navbar': base(request), 'user_detail': user_detail})
    else:
        return redirect('dangnhap')


def capnhattaikhoan(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_detail = Account.objects.get(user_id=user_id)
        if request.method == 'POST':
            user_update = Account.objects.filter(user_id=user_id)
            name = request.POST['name']
            sex = request.POST['sex']
            phone = request.POST['phone']
            email = request.POST['email']
            address = request.POST['address']
            birthday = request.POST['birthday']
            user_update.update(name=name, sex=sex, phone=phone, address=address, birthday=birthday)
            user_email = User.objects.get(pk=user_id)
            user_email.email = email
            user_email.save()
            if request.FILES.get('image', False):
                avatar = request.FILES['image']
                user_detail.avatar = avatar
                user_detail.save()
            return redirect('taikhoan')
        return render(request, 'user/taikhoan.html', {'navbar': base(request), 'user_detail': user_detail})
    else:
        return redirect('dangnhap')


@login_required(login_url='dangnhap')
def add_sp(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        prince = request.POST['prince']
        address = request.POST['address']
        type = request.POST['radiothueban']
        description = request.POST['description']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        Post(title=title, prince=prince, address=address, type=type, category=category, description=description).save()
        lastpost = Post.objects.latest('id')
        link = request.FILES['image']
        ImagePost(link=link, post=lastpost).save()
        return redirect('home')
    return render(request, 'user/post_add.html', {'navbar': base(request), 'category_list': category_list})


def sp(request, category_id=None, type=None):
    blog_list = News.objects.all().values('id', 'title', 'content', 'date_created', 'imagenews__link')[:5]
    if category_id == 0:
        sp_list = Post.objects.all().values('id', 'title', 'prince', 'category__name',
                                            'type', 'date_created', 'view', 'imagepost__link')
    else:
        sp_list = Post.objects.filter(category=category_id).values('id', 'title', 'prince', 'category__name',
                                                                   'type', 'date_created', 'view', 'imagepost__link')
    return render(request, 'user/sanpham.html', {'navbar': base(request), 'sp_list': sp_list, 'blog_list': blog_list})


def ctsp(request, post_id):
    post_detail = Post.objects.get(pk=post_id)
    post_detail.view += 1
    post_detail.save()
    image = ImagePost.objects.filter(post=post_id)
    return render(request, 'user/chitietsp.html', {'navbar': base(request), 'post_detail': post_detail, 'image': image})


def news(request):
    blog_list = News.objects.all().values('id', 'title', 'content', 'date_created', 'imagenews__link')
    return render(request, 'user/blog.html', {'navbar': base(request), 'blog_list': blog_list})


def news_detail(request, news_id):
    blog_list = News.objects.all().values('id', 'title', 'content', 'date_created', 'imagenews__link')[:5]
    blog_detail = News.objects.get(pk=news_id)
    image = ImageNews.objects.filter(news=news_id)
    return render(request, 'user/chitietblog.html',
                  {'navbar': base(request), 'blog_detail': blog_detail, 'image': image, 'blog_list': blog_list})
# End trang quản trị
