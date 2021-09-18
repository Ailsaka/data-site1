import importlib

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from dataSite1.projects import db


def view_projects(request, year=str(2020), p_name='gaoyuan'):
    # 外场数据默认页 (展示当前所有的数据表和字段名)
    print("项目管理默认页")
    print(p_name)

    project = importlib.import_module('.' + p_name, 'dataSite1.projects')
    project_list = db.project_list
    pic_url = 'projects/' + p_name + '.jpg'
    # pic = 'D:\\codeTemp\\PycharmProjects\\dataSite1\\static\\projects\\duitaizuozhan.jpg'
    flag = {}
    flag[p_name] = True

    dict_to_page = {
        'project_list': project_list,
        'p_char_name': project_list[year][p_name][0],
        'p_info': project_list[year][p_name][1].replace('\\n', '<br>'),
        'pic_url': pic_url,
        # 'year': year,
        # 'p_name': p_name,
    }
    print(dict_to_page)
    return render(request, "projects.html", dict_to_page)


def view_test(request):
    print('进入根项目主页面')
    # return HttpResponse()
    return render(request, "index.html", {'1': "1"})
# view 函数模板
# def func(request, _id=1):
#     try:
# 读取数据库数据可设置不同的数据库
#         _list = _.objects.using('default').all()
#         _item = _.objects.using('default').filter(id=_id)
#         dict_to_page = {
#             "db": get_db_info(),
#             "_id": _id,
#             "_list": _list,
#             "_item": _item,
#         }
#     except Task.DoesNotExist:
#         raise Http404("遇到了404错误，没有找到类表中的条目")
#     # 载入模板、填充上下文、生成HttpResponse对象
#     return render(request, "data/_.html", dict_to_page)
#
#     # HTTP 硬编码响应
#     return HttpResponse(
#                     ','.join(['123', '123'])
#             )
#


# models 类模型
# class (models.Model):
#     # 含义：
#     # mysql内自定义id
#     _id = models.IntegerField(default=0)
#     def __iter__(self):
#         for x in self.taskDesc:
#             print([x]])
#
#     # 可选
#     # 供命令行中的Task.objects.all() 调用
#     def __str__(self):
#         return self.task_text
