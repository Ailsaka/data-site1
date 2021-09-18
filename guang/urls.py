from django.urls import path
from . import views


app_name = 'guang'
urlpatterns = [

    # index login backend 
    path('index/', views.index, name='index'),
    path('login/', views.index, name='login'),
    path('backend/', views.index, name='backend'),
    # 画图
    path('charts/', views.index, name='charts'),
    path('charts/<str:info>/<int:axis>', views.charts, name='charts'),

    path('backend/<str:page>/', views.turn, name='backend'), 
    # backend/table-list.html/tag_xx
    path('backend/<str:page>/<str:info>', views.turn, name='backend'),
    # 新建表
    path('backend/<str:parentpage>/<str:page>/<str:info>', views.turn, name='backend'),


    # 测试函数
    path('test/', views.test, name='test'),

    # ex:/assetinfo/test_django_excel_upload
    path('test_django_excel_upload/', views.TestDjangoExcelUpload.as_view() , name='test_django_excel_upload'),

    # ex:/assetinfo/test_django_excel_download
    path('test_django_excel_download/', views.TestDjangoExcelDownload.as_view() , name='test_django_excel_download'),

    
    # tables/change_state/0 1 2 3 -1
    path('tables/', views.entity_opr, name='tables'),
    path('tables/<str:opr>', views.entity_opr, name='tables'),

    path('tables/<str:opr>/<str:info>', views.entity_opr, name='tables'),
    
    path('cols/', views.entity_opr, name='cols'),
    path('cols/<str:opr>', views.entity_opr, name='cols'),
    
    path('values/', views.entity_opr, name='values'),
    path('values/<str:opr>', views.entity_opr, name='values'),

    path('department/', views.entity_opr, name='department'),
    path('department/<str:opr>', views.entity_opr, name='department'),


    path('index/1/<str:page>/', views.turn, name='turn_to_page'),
    path('index/1/<str:parent>/<str:page>/', views.turn, name='turn_to_page'),
    path('index/1/<str:parent>/<str:page>/<str:info>/', views.turn, name='turn_to_page'),
    path('index/1/<str:parent>/<str:page>/<str:info>/<str:user>', views.turn, name='turn_to_page'),

    path('index/2/<str:page>/', views.turn, name='turn_to_page'),
    path('index/2/<str:parent>/<str:page>/', views.turn, name='turn_to_page'),
    path('index/2/<str:parent>/<str:page>/<str:info>/', views.turn, name='turn_to_page'),
    path('index/2/<str:parent>/<str:page>/<str:info>/<str:user>', views.turn, name='turn_to_page'),
]
