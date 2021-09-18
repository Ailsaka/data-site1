import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class DataManager(models.Manager):
    # 自定义查询语句
    def query_all(self):
        from django.db import connection
        from django.apps import apps
        with connection.cursor() as cur:
            str = apps.get_models()
            cur.execute()


class Table(models.Model):
    name = models.CharField(default='', max_length=20, verbose_name='表名')
    desc = models.CharField(default='', max_length=50, verbose_name='说明信息')
    # state: 0 编辑 1 启用 2 停用 3 删除  （-1  彻底删除表结构和数值）
    state = models.CharField(default='0', max_length=2, verbose_name='发布状态')
    tag = models.CharField(default='默认类别', max_length=10, verbose_name='类别')
    update = models.DateTimeField(default=datetime.datetime.now(), verbose_name='更新时间')

    # 定c1为关键列
    c0 = models.IntegerField(default=0, \
        validators=[MinValueValidator(1),\
                    MaxValueValidator(100)], \
                    verbose_name='列的数量')
    for i in range(1, 101):
        # locals()[]
        exec("c%s=\
            models.CharField(default='默认列名', max_length=20, verbose_name='列名')\
            " % str(i))
    objects = DataManager()

    # def __unicode__(self):
    #     print("表名：{0} \n描述信息: {1} \n字段: {2}".format(self.name, self.desc, [f+'|'+f.verbose_name for f in self._meta.fields]))

class Tag(models.Model):
    # 分类依据 'tag'
    name = models.CharField(default='默认类别', max_length=10, verbose_name='类别')
    tables_under_tag = models.IntegerField(default=0, verbose_name='当前表数量')

    # 弃之不用
# class Col(models.Model):
#     table = models.ForeignKey(Table, on_delete=models.CASCADE)
#     name = models.CharField(default="", max_length=20, verbose_name="列名")
#     desc = models.CharField(max_length=50, default="", verbose_name='类型定义')
#     update = models.DateTimeField(default=datetime.datetime.now(), verbose_name='更新时间')
#     objects = DataManager()


class Department(models.Model):
    name = models.CharField(default="", max_length=20, verbose_name="部门")
    objects = DataManager()


class Value(models.Model):
    # 某个实体属性的具体值，均用字符串记录，在函数中解析 每年分表
    # date   datetime。。。
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    update = models.DateTimeField(default=datetime.datetime.now(), verbose_name='更新时间')

    for i in range(1, 101):
        # locals()[]
        exec("v%s=\
            models.CharField(default='默认值', max_length=50, verbose_name='数据值')\
            " % str(i))

    objects = DataManager()

    class Meta:
        verbose_name = "具体值"
        verbose_name_plural = "具体值"


def get_table_model(prefix):
    table_name = "guang_%s" % prefix

    class GuangMetaClass(models.base.ModelBase):
        def __new__(cls, *args, **kwargs):
            # name += '_' + prefix
            return models.base.ModelBase(cls, *args, **kwargs)

    # class ():
        
    return 0
