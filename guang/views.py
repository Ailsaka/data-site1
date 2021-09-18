# --内置模块-- #
import datetime
import json
import random   

from django.core import serializers
from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render

from django.views.generic import View
from django import forms
import pyexcel as pe
import django_excel as excel
import xlsxwriter

from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt


# --模型-- #
from guang.models import *

# --测试组件-- #
from django_seed import Seed

# --自定义工具-- #
from guang.tools import *
from guang.test_tools import *

models_dict = {
    'table':Table,
    'tag':Tag,
    'department':Department,
}




@csrf_exempt
def index(request):
    print("_________view_index___________")
    page = request.path[7:-1]
    dict_to_page = get_dict(page)
    return render(request, "guang/"+page+".html", dict_to_page)

def charts(request, info=None, axis=None):
    print("_________view_charts___________\n"+info)
    dict_to_page = {
    't_count': Table.objects.count(),
    'v_count': Value.objects.count(),
    'this_week': Value.objects.filter(update__gte=\
        datetime.datetime.now()-datetime.timedelta(days=7)).count(),
    'this_week_update': [],
    }

    if info:
        tables = {}
        for table in Table.objects.filter(id__in=info.split(',')):
            tables[table.name] = {'cols': get_col_list(table), 'values':get_value_list(table),}
            # for i in range(1, table.c0+1):
            #     exec("tables[table.name]['cols'].append(table.c%s)" % (i))
            # for value in Value.objects.filter(table=table):
            #     v_s = []
            #     for i in range(1, table.c0+1):
            #         exec("v_s.append(value.v%s)" % (i))
            #     tables[table.name]['values'].append(v_s)

            try:
                # 处理数字型字段
                int(values)
            except ValueError as e:
                try:
                    # 处理字符串字段
                    pass
                except Exception as e:
                    pass
            for value in Value.objects.filter(table=table):
                pass
        dict_to_page['tables'] = tables


    return render(request, "guang/charts.html", dict_to_page)

def get_dict(page, argv=None):
    if page == 'backend':
        return {'tags': Tag.objects.values('name')}
    pass



def test(request):
    # update_model('value', 'c1')
    # insert_huge_amount()

    return HttpResponse()

@csrf_exempt
def entity_opr(request=None, entity=None, opr=None, my_data_dict=None, info=''):
    
    obj_dict = {}
    flag_ok = False

    if request:
        if request.path.__contains__('table'):
            entity = 'table'
        elif request.path.__contains__('col'):
            entity = 'col'
        elif request.path.__contains__('value'):
            entity = 'value'
        elif request.path.__contains__('department'):
            entity = 'department'
        
        try:
            request_dict = json.loads(request.body.decode('utf-8'))
            ids = request_dict.get('ids')
            state = request_dict.get('state')
            print('解码request{} {} {}'.format(request_dict, ids, state))
        except Exception:
            ids = request.POST.get('ids')
            state = request.POST.get('state')
            print('直接读取request {} {}'.format(ids, state))
        finally:
            obj_dict = {
                'name': request.POST.get('name'),
                'desc': request.POST.get('desc'),
                'update': datetime.datetime.now(),
            }     

    print('操作开始opr: {}, \nentity: {}, \nobj_dict: {}\nmy_data_dict: {}'.format(opr, entity, obj_dict, my_data_dict))


    if opr == 'edit':
        print("try edit: {}, obj_dict: {}".format(ids, obj_dict))
        if entity == 'table':
            for id in ids:
                table = Table.objects.get(id=id)
                table.name = obj_dict['name']
                table.desc = obj_dict['desc']
                table.update = obj_dict['update']
                table.save()
        elif entity == 'col':
            col = Col.objects.get(id=ids)
            col.name = obj_dict['name']
            col.desc = obj_dict['desc']
            col.update = obj_dict['update']
            col.save()
    elif opr == 'change_state':
        print("修改ids: {}, \n修改后状态: {}".format(ids, state))
        if state == '-1':
            # 彻底删除表结构和数值 会删除引用此表的数值记录
            tables = Table.objects.filter(id__in=ids)
            for table in tables:
                tag = Tag.objects.get(name=table.tag)
                tag.tables_under_tag -= 1
                tag.save()
                if tag.tables_under_tag <= 0:
                    print("删除类别{}，\n影响了{}行".format(tag.name, tag.delete()))
                else:
                    print("{}类别下还有{}个表".format(tag, tag.tables_under_tag))
            print("删除表{}，\n影响了{}行".format(tables, tables.delete()))
        else :
            for id in ids:
                table = Table.objects.get(id=id)
                table.state = state
                table.save()
        flag_ok = True

    elif opr == 'add':
        if entity == 'value':
            # 提交单条数据
            new_value = Value.objects.create(**my_data_dict)
            new_value.save()
            flag_ok = True
        elif entity == 'department':
            department, created = Department.objects.get_or_create(name=obj_dict['name'])

    elif opr == "del":
        print('try del: {}'.format(ids))
        models_dict[entity].objects.filter(id__in=ids).delete()

    elif opr == "test":
        print('test')
        return render(request, "guang/admin/index.html", {'result': "success" + opr})
    else:
        tables = {
            '表1': ["字段1", "字段2", "字段3"],
            '表2': ["字段1", ],
            '表3': ["字段1", "字段2", "字段3", "字段4", "字段5"],
        }

    print('操作开始opr: {}, \nentity: {}, \nobj_dict: {}\nmy_data_dict: {}'.format(opr, entity, obj_dict, my_data_dict))
    if request:
        return HttpResponse("完成操作")
    else:
        return flag_ok


def turn(request, parentpage=None, page=None, info=None, user=None):
    dict_to_page = {'cols':[],'values':[]}
    root_url = request.path.split('/')[2]
    print("*------收到千台请求，进入后台--------*")
    print("request: %s" % request)
    print("request: %s" % request.path)
    print("parentpage: %s" % parentpage)
    print("page: %s" % page)
    print("info: %s" % info)
    print("user: %s" % user)
    print("root_url: %s" % root_url)
    if parentpage:
        # ('两级url，含两个.html')
        try:
            table = Table.objects.get(id=info)
            dict_to_page['table'] = table
            dict_to_page['cols'].extend(get_col_list(table))
            # for i in range(1, table.c0+1):
            #     exec("dict_to_page['cols'].append(table.c%s)" % str(i))
        except:
            pass

        if page.__contains__('table-list.html'):
            pass
        elif page.__contains__('value-list.html'):
            # 查看数据
            dict_to_page['values'].extend(get_value_list(table))
            # values = Value.objects.filter(table=table)
            # for value in values:
            #     temp_list = []
            #     for i in range(1, table.c0+1):
            #         exec("temp_list.append(value.v%s)" % str(i))
            #     dict_to_page['values'].append(temp_list)
            page = 'value-list.html'
        elif page.__contains__('table-add-edit.html'):
            # 打开创建新表/修改旧表的页面 需提供所有的tag供选择 
            dict_to_page['tags'] = Tag.objects.values('name')
        elif page.__contains__('value-upload.html'):
            # 增加单条数据、批量上传
            dict_to_page['ids'] = info
            dict_to_page['departments'] = Department.objects.values('name')
    else:
        # ('一级url，含1个.html')
        if page.__contains__('table-list.html'):
            try:
                if info.__contains__('tag_'):
                    # 特定类别的表 backend/table-list.html/tag_xx
                    tag_name = info[4:]
                    dict_to_page['tag_name'] = tag_name
                    dict_to_page['tables'] = Table.objects.filter(tag=tag_name)
                    info = 'tag_'
                    # .exclude(state='3')
                elif info.__contains__('valid'):
                    # 所有发布可填写的表
                    dict_to_page['tables'] = Table.objects.filter(state='1')
                elif info.__contains__('available'):
                    # 所有编辑中的表
                    dict_to_page['tables'] = Table.objects.filter(state='0')
                elif info.__contains__('stop'):
                    # 所有停用的表
                    dict_to_page['tables'] = Table.objects.filter(state='2')
                elif info.__contains__('del'):
                    # 所有删除的表
                    dict_to_page['tables'] = Table.objects.filter(state='3')
                elif info.__contains__('for_chart'):
                    # 供选择，画图
                    # cols  第100号表的001列  100001: 
                    dict_to_page['tables'] = Table.objects.all()
                    dict_to_page['cols'] = {}
                    for table in dict_to_page['tables']:
                        dict_to_page['cols'][table.id] = get_col_dict(table)

                dict_to_page.setdefault('info', info)
            except Exception as e:
                print(e)
                dict_to_page['tables'] = Table.objects.all()
        elif page.__contains__('department-list.html'):
            dict_to_page['departments'] = Department.objects.all()
        

        # elif page.__contains__('index.html'):
        #     print("登陆验证user: {}, pwd: {}".format(request.POST.get('1'), request.POST.get('2')))
        #     # 返回表格的分类
        #     dict_to_page['tags'] = list(State.objects.all())
        # elif page.__contains__('value-edit.html'):
        #     dict_to_page['values'] = Value.objects.filter(table__id=info)
        # elif page.__contains__('ajax'):
        #     if request.POST.get('table_names'):
        #         return HttpResponse(json.dumps(Table.objects.only('name')), content_type='application/json')
    print('→→→→→→→\nturn to: {}\ndict_to_page: {}'.format(page, dict_to_page))
    return render(request, "guang/"+root_url+"/"+page, dict_to_page)


class UploadFileForm(forms.Form):
    file = forms.FileField()

# ex:/assetinfo/test_django_excel_upload
class TestDjangoExcelUpload(View):
    """测试使用django-excel上传文件"""

    def get(self,request):
        form = UploadFileForm()
        return render(request,'upload_form.html',context={ 'form': form })

    def post(self,request):
        print("=----收到了前端上传的文件(post)----=\nrequest: {0}\n".format(request.POST))
        form = UploadFileForm(request.POST, request.FILES)
        my_data_dict = {'update': datetime.datetime.now()}

        # 提取公共参数            
        try:
            # 表的参数
            my_data_dict['name'] = request.POST['name']
            my_data_dict['desc'] = request.POST['desc']
            if request.POST['tag_input'].strip() != '':
                my_data_dict['tag'] = request.POST['tag_input']
            else:
                my_data_dict['tag'] = request.POST['tag_choice']
            tag, created = Tag.objects.get_or_create(name=my_data_dict['tag'])
            if created:
                tag.tables_under_tag = 1
                tag.save()
            else:
                tag.tables_under_tag += 1
                tag.save()
            my_data_dict["c0"] = 0
        except KeyError:
            # 值的参数
            my_data_dict['table'] = Table.objects.get(id=request.POST.get('ids', "1"))
            my_data_dict['department'], created = Department.objects.get_or_create(\
                name=request.POST.get('department_choice', "默认车间"))
            for i in range(1, my_data_dict['table'].c0+1):
                exec("col_name = my_data_dict['table'].c%s" % str(i))
                value = request.POST.get('value_' + locals()['col_name'])
                if len(value) > 0:
                    my_data_dict['v'+str(i)] = value

        if form.is_valid():
            fileHandle = request.FILES['file']
            try:
                # 解析列名  不是表-则my_data_dict["c0"]报错KeyError
                cols = fileHandle.get_sheet().row_at(0)
                my_data_dict["c0"] = my_data_dict["c0"] + len(cols)
                for i, col in enumerate(cols):
                    exec("my_data_dict['c%s'] = col" % (str(i+1)))
                try:
                    # 有id  修改旧表
                    table = Table.objects.get(id=request.POST['ids'])
                    table.name = my_data_dict['name']
                    table.tag = my_data_dict['tag']
                    table.desc = my_data_dict['desc']
                    table.update = my_data_dict['update']
                    table.c0 = my_data_dict['c0']
                    for i, col in enumerate(cols):
                        exec("table.c%s = col" % (str(i+1)))
                    table.save()
                    return HttpResponse("修改完成")
                except Exception as e:
                    print(e)
                    # 没有id  创建新表
                    try: 
                        Table.objects.get(name=my_data_dict['name'])
                        return HttpResponse("创建失败，表名冲突，请尝试修改")
                    except Table.DoesNotExist :
                        table = Table.objects.create(**my_data_dict)
                        table.save()
                        return HttpResponse("新建完成")
            except KeyError:
                # 批量上传值
                table = Table.objects.get(id=request.POST['ids'])
                records = fileHandle.get_sheet().get_records()
                for record in records:
                    print(record)
                return HttpResponse("数据已上传")

        else:
            # 未上传excel文件，是否修改了类别、描述、表名
            try:
                Table.objects.filter(id=request.POST['ids']).update(
                    name = my_data_dict['name'],
                    tag = my_data_dict['tag'],
                    desc = my_data_dict['desc'],
                    update = my_data_dict['update']
                )
                return HttpResponse("修改完成")
            except (AttributeError, KeyError):
                # 提交单条数据
                entity_opr(request=None, entity='value', opr="add", my_data_dict=my_data_dict)
                return HttpResponse("数据已提交")
            else:
                print(e)
                return HttpResponseBadRequest("<h3>缺少excel文件</h3>")


# ex:/assetinfo/test_django_excel_download
class TestDjangoExcelDownload(View):
    """测试使用django-excel下载文件"""

    def get(self, request):
        print("=----收到了前端的文件下载请求(get)----=\nTestDjangoExcelDownload\nrequest: {0}\n".format(request.GET))
    # try:
        ids = request.GET.get('ids').split('.')
        pe_book_dict = {}

        for table in Table.objects.filter(id__in=ids):
            pe_book_dict[table.name] = [[], ]
            pe_book_dict[table.name][0].extend(get_col_list(table))
            # for j in range(1, table.c0+1):
            #     exec("pe_book_dict[table.name][0].append(table.c%s)" % (j))
            for i, value in enumerate(Value.objects.filter(table=table)):
                pe_book_dict[table.name].append([])
                for j in range(1, table.c0+1):
                    exec("pe_book_dict[table.name][i+1].append(value.v%s)" % (j))

        pe_book = pe.get_book(bookdict=pe_book_dict)
        return excel.make_response(pe_book, "xlsx")
    # except Exception as e :
    #     print(e)
    #     sheet = excel.pe.Sheet([[1, 2], [3, 4]])
    #     # 文件格式支持xlsx\xls\csv
    #     return excel.make_response(sheet, "csv", file_name='出错了')
    #     return HttpResponse(e)

    @csrf_exempt
    def post(self, request):
        print("=----收到了前端的文件下载请求(post)----=\nTestDjangoExcelDownload\nrequest: {0}".format(request.POST))
        # request.POST为QueryDict类型  只有1对键值对   ajax的data为键   值为空
        # {ids:, state:}
        # 生成器 request.POST.items()
        dispatch = next(request.POST.items())[0]
        ajax_dict = json.loads(dispatch)
        print("下载表： ", ajax_dict['ids'])

        # ids = ""
        # for idi in ajax_dict['ids']:
        #     ids += "id_=" + idi
        ids = ".".join(ajax_dict['ids'])
        return HttpResponse(ids)

