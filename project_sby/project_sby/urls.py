from django.contrib import admin
from django.urls import path, re_path
# from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from app_sby import views

urlpatterns = [
    # Trang quản trị
    # Trang admin django
    path('010821/', admin.site.urls),
    # ------------------
    # Tổng quan
    path('admin/', views.root_home, name='root_home'),
    # ------------------
    # Bài đăng
    path('postadd/', views.root_post_add, name='post_add'),
    path('postlist/', views.root_post_list, name='post_list'),
    path('post_add_process/', views.root_post_add_process, name='post_add_process'),
    path('post_update_process/<int:post_id>/', views.root_post_update_process, name='post_update_process'),
    path('post_update_delete/<int:post_id>/', views.root_post_delete_process, name='post_delete_process'),
    # ------------------
    # Danh mục
    path('category/', views.root_category, name='category'),
    path('category_add/', views.root_category_add, name='category_add'),
    path('category_update/<int:category_id>/', views.root_category_update, name='category_update'),
    path('category_delete/<int:category_id>/', views.root_category_delete, name='category_delete'),
    # ------------------
    # Tin tức
    path('rootnews/', views.root_news, name='root_news'),
    path('newsadd/', views.root_news_add, name='news_add'),
    path('newsaddprocess/', views.root_news_add_process, name='news_add_process'),
    path('newsupdateprocess/<int:news_id>/', views.root_news_update_process, name='news_update_process'),
    path('newsdelete/<int:news_id>/', views.root_news_delete, name='news_delete'),
    # Phản hổi
    path('rootfeedback/', views.root_feedback, name='root_feedback'),
    # End trang quản trị

    # Trang khách hàng
    path('', views.home, name='home'),
    path('private/', views.private, name='private'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('doitac/', views.doitac, name='doitac'),
    path('dangnhap/', views.dangnhap, name='dangnhap'),
    path('dangky/', views.dangky, name='dangky'),
    path('dangxuat/', views.dangxuat, name='dangxuat'),
    path('taikhoan/', views.taikhoan, name='taikhoan'),
    path('capnhattk/', views.capnhattaikhoan, name='capnhattk'),
    path('addsp/', views.add_sp, name='addsp'),
    path('sp/', views.sp, name='sp'),
    path('sp/<int:category_id>/', views.sp, name='sp'),
    path('ctsp/<int:post_id>/', views.ctsp, name='ctsp'),
    path('news/', views.news, name='news'),
    path('news_detail/<int:news_id>/', views.news_detail, name='news_detail'),
    # End trang khách hàng
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
