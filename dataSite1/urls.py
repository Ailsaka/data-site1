from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from . import views, settings


urlpatterns = [
    path('', views.view_test, name="url_main_page"),
    # 图标
    url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
    # 后台
    path('admin/', admin.site.urls, name="url_admin"),

    # 项目管理看板
    # path('projects/', views.view_projects, name='url_projects'),
    # path('projects/<str:p_name>', views.view_projects, name='url_projects'),
    # path('projects/<str:year>/<str:p_name>', views.view_projects, name='url_projects'),

    #
    path('guang/', include('guang.urls'), name="url_guang"),

    # 用于处理static里的文件 部署用
    # path(r'static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}, ),

]
