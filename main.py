import datetime
import os
import re
import time

# import jieba


def dict_arg(**filters):
    print(filters)
    pass


dict_arg(a=1, b=2, c=3)


def tuple_arg(*filters):
    print(filters)
    pass


tuple_arg(1, 2, 3, )

if __name__ == '__main__':
    print('Hello!')

    dict1 = {
        'name': 1,
        'pass': 2,
    }
    print(str(dict1))

    # 网络爬取
    # import urllib.request
    # with urllib.request.urlopen('http://192.168.5.1:8080/general/index.php?isIE=0') as req:
    #     data = req.read()
    # print('Status:', req.status, req.reason)
    # for k, v in req.getheaders():
    # print('{:A>8s}__________{:A>8s}'.format(k, v))
    # print('%s _____________ %s' % (k, v))
    # print(data.decode('gb2312'))

    # 交换
    # s = 'fufufuf'
    # s1 = 'aaa'
    # a, b = 1, 2
    # a, b, s, s1 = b, a, s1, s
    # print(a, b, s, s1)

    # 格式化字符串
    # template = '{:*<5d}_______{:.9f}______'
    # template = '{0:5d}_______{1:.5f}______{2:*>.6s}___'
    # print(template.format(11, 1.2, 'sss'))

    # 内置排序
    # sb = {i for i in range(7, 15)}
    # print(sorted(sb))
    # s_list = ['string', 'lily', 'abc', 'catherine', 'dark', 'can']
    # s_list.sort(key=lambda x: (1 / len(list(x))))
    # print(s_list)
    # d = {
    #     '1992': [1, 2, 3],
    #     '1932': [1, 2, 4],
    #     '2019': [1, 2, 6],
    #     '2001': [1, 2, 3],
    #     '2039': [1, 2, 3],
    #     '2022': [1, 2, 3],
    # }
    # for num, content in enumerate(d):
    #     print(num)
    #     print(content)
    # d1 = [k for k in sorted(d.keys())]
    # d2 = [v for v in sorted(d.values())]
    # print(d1)
    # print(d2)
    # d3 = sorted(d.items(), key=lambda x: x[0], reverse=True)
    # d4 = sorted(d.items(), key=lambda x: x[1], reverse=True)
    # print(d3)
    # print(d4)

    # 迭代器
    # d = {
    #     '1992': [1, 2, 3],
    #     '1932': [1, 2, 4],
    #     '2019': [1, 2, 6],
    #     '2001': [1, 2, 3],
    #     '2039': [1, 2, 3],
    #     '2022': [1, 2, 3],
    # }
    # it = iter(d)
    # l = (i**2 for i in range(1, 20))
    # print(l)
    # year_last_num = lambda x: x[3]
    # for last_num, x in itertools.groupby(d.keys(), year_last_num):
    #     print((last_num, tuple(x)))
    # i = 0
    # for xx in itertools.combinations(d, 3):
    #     i += 1
    #     print(set(xx), end='        _{}\n'.format(i))
    # i = 0
    # for xxx in itertools.permutations(d, 3):
    #     i += 1
    #     print(xxx, end='________{}\n'.format(i))

    # 列表
    # l = collections.deque
    # ll = [1, 2, 3]
    # ll.pop()
    # ll.insert(0, 0)
    # ll.extend([9, 9, 9, 9, 9])
    # print(ll)

    # 元组
    # tup = (1, ), (2, )
    # tup1 = (10, ) + (20, )
    # tup2 = tup1 * 5
    # (a, ), (b, ) = tup
    # c, d = tup1
    # print(tup)
    # print(a, b)
    # print(tup1)
    # print(c, d)
    # print(tup2)

    # 集合
    # sa = {i for i in r0ange(10)}
    # print(sa)
    # for i in range(0, 5):
    #     print(sb.pop())
    #     print(sb)

    # 字典
    # 配对
    # for i, v in zip(range(0, 5), range(10, 20)):
    #     print(i)
    #     print(v)
    # for i, v in enumerate(zip(range(0, 5), range(10, 20))):
    #     print(i)
    #     print(v)
    # 利用2-元组创建字典
    # mapping = dict(zip(range(0, 5), reversed(range(0, 5))))
    # print(mapping)
    # d = {
    #     'a': 'asdfg',
    #     'b': 'bvcz',
    #     'c': 'cccccc',
    #     'd': 'dddddd',
    #     'e': 'eeeee',
    #     'f': 'fff',
    #     'm': 'mmf',
    #     'n': 'nmf',
    #     'h': 'hmf',
    # }
    # v = d.get('x', '没找到！')
    # print(v)
    # d1 = {}
    # for value in d.values():
    #     key_word = value[-1:]
    #     # if key_word not in d1:
    #     #     d1[key_word] = []
    #     # d1[key_word] = value
    #     d1.setdefault(key_word, []).append(value)
    # print(d1)

    # 文件处理
    # BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    # BASE_PATH1 = os.path.join(BASE_PATH, '1.txt')
    # f_main = open(BASE_PATH1, 'r')
    # try:
    #     for i in reversed(range(1, 10)):
    #         f_main.write(str(i)*10 + '\n')
    # except Exception as e:
    #     print(e)
    # finally:
    #     print('不管是否有异常，一定会执行的代码')
    #     f_main.close()
    # with open(BASE_PATH2) as f_test:
    #     print(f_test.readlines())
    # lines = [x for x in open(BASE_PATH2)]
    # print(lines)

    import shutil
    # 将所有文件拷贝到一个文件夹 有重名文件保留 核对文件个数、大小
    # dst_path = "D:\\yx（秘密）\\原始数据\\"
    # src_path = "D:\\yx（秘密）\\原始数据\\test"
    # src_list = []
    # filter_list = ['民融合', '装外军', '厂军', '建设',
    #                '合同', '购买', '北京', '西安', '发动机', '参数', '寿命', '信号',
    #                '综合调节器', '综调',
    #                '推荐书', '规定', '图', '培训', '技术条件',  '任务书', '材料', '简介',
    #                '大纲', '修理方案', '手册', '研制', '科研', '测试', '延寿',
    #                '规程', '指南', '规划', '检验', '申请', '通报', '可行性', '原理', '结论',
    #                '活门', '惯导', '故障统计', '工作时序',
    #                '报价', '清册', '活动方案', '学习', '串件', '纪要', '方案', '评审', '管理', '心得', '体会', '感受', '感悟',
    #                '李嘉', '黄彩云', '殷龙文', '宁凯诚', '强柯', '唐景凡', '孙嘉诚',
    #                ]
    # in_list = ['靶试', '打靶', '失利', '命中', '未发射', '脱靶', '挂飞', '精准']
    # f_moved = 0
    # for root, dirs, media_files in os.walk(src_path):
    #     for f in media_files:
    #         try:
    #             # # 1.
    #             # fii = open(root + '\\' + f, 'rb')
    #             # fj = open(root + '\\' + f, 'wb')
    #             # for line in fii:
    #             #     fj.write(line)
    #             # fii.close()
    #             # fj.close()
    #             # # 2.方法二
    #             dst_files = set(os.listdir(dst_path))
    #             if f not in dst_files:
    #                 shutil.move(os.path.join(root, f), os.path.join(dst_path, f))
    #             else:
    #                 shutil.move(os.path.join(root, f), os.path.join(dst_path, f) +
    #                             datetime.datetime.utcnow().strftime('-%S%f'))
    #             # 3.
    #             # flag_in = False
    #             # for in_word in in_list:
    #             #     if f.find(in_word) >= 0:
    #             #         flag_in = True
    #             # if flag_in:
    #             #     continue
    #             # for filter_word in filter_list:
    #             #     if f.find(filter_word) >= 0:
    #             #         shutil.move(root + '\\' + f, dst_path + '\\' + f)
    #             #         f_moved += 1
    #             #         continue
    #             # 4.
    #             # src_list.extend(jieba.lcut(f))
    #         except Exception as e:
    #             print(e)
    #
    # print('file moved: %s' % f_moved)
    # counts = {}
    # for word in src_list:
    #     if len(word) == 1:
    #         continue
    #     counts[word] = counts.get(word, 0) + 1
    # print(counts)
    # d2 = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # for x in d2:
    #     f_main.write(x[0] + '\t' + str(x[1]) + '\t' + '\n')

    # 按文件类型分到各个文件夹
    # src_path = "D:\\yx（秘密）\\原始数据\\test-seperate"
    # dst_path = "D:\\yx（秘密）\\原始数据"
    # for root, dirs, media_files in os.walk(src_path):
    #     for f in media_files:
    #         try:
    #             shutil.move(os.path.join(root, f),
    #                         dst=os.path.join(dst_path+'\\'+f.split('.')[-1], f))
    #         except FileNotFoundError:
    #             os.mkdir(dst_path + '\\' + f.split('.')[-1])
    #             shutil.move(os.path.join(root, f),
    #                         dst=os.path.join(dst_path+'\\'+f.split('.')[-1], f))
    #         except PermissionError:
    #             print(os.path.join(root, f))

    # import docx
    # 读取处理文档-docx
    # dst_path = "D:\\yx（秘密）\\原始数据"
    # src_path = "D:\\yx（秘密）\\原始数据\\test\\doc"
    # for root, dirs, media_files in os.walk(src_path):
    #     for f in media_files:
    #         if f[0] != '_':
    #             continue
    #         try:
    #             file = docx.Document(os.path.join(root, f))
    #             # file_txt = open(dst_path + '\\' + '{}.txt'.format(f[::-1].split('.', 1)[-1][::-1]), 'w')
    #             for p in file.paragraphs:
    #                 for mno in re.findall(r'\d+', p.text):
    #                     f_main.write(mno+'\n')
    #             f_main.write('###'+root+'\\'+f+'\n')
    #         except Exception as e:
    #             print('?????????')
    #             print(e)
    #             print(root + '\\' + f)

    # 读取处理文档-doc 0kb 、文不对题
    # import win32com.client as wc
    # dst_path = "C:\\bqwebrelease\\转docx"
    # src_path = "C:\\bqwebrelease\\已发\\doc"
    # for root, dirs, media_files in os.walk(src_path):
    #     for f in media_files:
    #         try:
    #             word = wc.Dispatch("Word.Application")
    #             doc = word.Documents.Open(os.path.join(root, f))
    #             doc.SaveAs(dst_path + '\\' + f[::-1].split('.', 1)[-1][::-1] + '.docx',
    #             12, False, "", True, "", False, False, False, False)
    #             doc.Close()
    #             word.Quit()
    #         except Exception as e:
    #             print(e)
    #             print(root + '\\' + f)
    #             f_main.write(root + '\\' + f + '\n')





    s = """01-05-64-001和13-04-64-030过
    01/100-0612-032、  01-10-64-017是是是
    03-06-64-009和03-06-64-026
    """
    # for x in re.findall('[[0-9]{2}-]{3}[0-9]{3}', s):
    # for x in re.findall(r'\d\d-\d\d-\d\d-\d\d\d', s):
    #     print(x)
    # for x in re.findall(r'\d\d/\d\d\d-\d\d\d\d-\d\d\d', s):
    #     print(x)
    # for line in f_main:
    #     # temp_list = re.findall('[[0-9]{2}-]{3}[0-9]{3}', line)
    #     temp_list = re.findall(r'\d\d\d\d', line)
    #     for x in temp_list:
    #         print(x)
    #     temp_list = re.findall(r'\d\d\d\d\d\d', line)
    #     for x in temp_list:
    #         print(x)

    import pdfminer

    # f_main.close()



