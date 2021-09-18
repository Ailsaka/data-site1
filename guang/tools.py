import datetime, random
from guang.models import * 

# 获取范围内的随机时间
def randdom_time(start, end, n=1, frmt="%Y-%m-%d %H:%M:%S"):
	stime = datetime.datetime.strptime(start, frmt)
	etime = datetime.datetime.strptime(end, frmt)
	if n == 1:
		time_datetime = random.random() * (etime - stime) + stime
	else:
		time_datetime = [random.random() * (etime - stime) + stime\
		for _ in range(n)]
	return time_datetime



# 根据table取所有列名
def get_col_list(table):
	c_list = []
	for i in range(1, table.c0+1):
		exec("c_list.append(table.c%s)" % (i))
	return c_list

def get_col_dict(table):
	c_dict = {}
	for i in range(1, table.c0+1):
		exec("c_dict[i] = (table.c%s)" % (i))
	return c_dict

def get_value_list(table):
	v_list = []
	for value in Value.objects.filter(table=table):
		v_l = []
		for i in range(1, table.c0+1):
			exec("v_l.append(value.v%s)" % (i))
		v_list.append(v_l)
	return v_list


# 字符串合法判断，去除非法值、空值
def remove_null(temp_str):
	return temp_str.strip()

if __name__ == '__main__':
	print(randdom_time('2020-1-1 0:0:0', '2022-1-1 0:0:0'))