from django.http import HttpResponse
from django.shortcuts import redirect


def kiemtradangnhap(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def kiemtraquyenadmin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('Bạn không đủ quyền truy cập.')
    return wrapper_func


# def chapnhan(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles or request.user.is_superuser:
#                 return view_func(request, *args, **kwargs)
#             else:
#
#         return wrapper_func
#     return decorator
