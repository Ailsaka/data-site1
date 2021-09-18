# !/usr/bin/env python3
# encoding utf-8



"测试用的各种函数"


__author__ = ""





# --内置模块-- #
import datetime
import json
import random 

# --模型-- #
from guang.models import *

models_dict = {
    'table':Table,
    'tag':Tag,
    'department':Department,
}

def print_request(request):
    print()
    for k, v in request.environ.items():
        print(k, v)



def update_model(model_name, col_name, \
    int_value=random.random()*100+1, \
    str_value=random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'), \
    date_value=datetime.datetime.now()):
    # 修正字段值
    try:
        for model_x in models_dict[model_name].objects.all():
            exec("model_x.%s=int_value" % (col_name))
            model_x.save()
    except:
        try:
            for model_x in models_dict[model_name].objects.all():
                exec("model_x.%s=str_value" % (col_name))
                model_x.save()
        except Exception as e:
            try:
                for model_x in models_dict[model_name].objects.all():
                    exec("model_x.%s=date_value" % (col_name))
                    model_x.save()
            except Exception as e:
                raise e
          
def insert_huge_amount():
    # 批量insert
    seeder = Seed.seeder()
    seeder.add_entity(Value, 50, {
        'table': Table.objects.get(id=random.randint(15, 23)),
        'department': Department.objects.get(id=random.randint(7, 12)),
        'update': randdom_time('2020-1-1 0:0:0', '2022-1-1 0:0:0'),
        })
    seeder.add_entity(Table, 50, {
        'name': seeder.faker.name(),
        'desc': seeder.faker.text(),
        'state': lambda x: random.randint(0, 3),
        'tag': Tag.objects.get(id=random.randint(10, 13)).name,
        'c0': lambda x:random.randint(1, 100),
        'update': randdom_time('2020-1-1 0:0:0', '2022-1-1 0:0:0'),
        })
    inserted_pks = seeder.execute()
    return inserted_pks

if __name__ == '__main__':
	test()

